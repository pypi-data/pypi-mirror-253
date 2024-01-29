import functools
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import List, Optional, Tuple

import bpkio_cli.utils.scte35 as scte35
import bpkio_cli.utils.sounds as sounds
import click
import m3u8
import progressbar
from bpkio_api.helpers.handlers.hls import HLSHandler
from bpkio_cli.writers.colorizer import Colorizer as CL
from bpkio_cli.writers.colorizer import trim_or_pad
from bpkio_cli.writers.scte35 import summarize
from tabulate import tabulate
from threefive import Cue, SegmentationDescriptor


class SignalType(Enum):
    PERIOD = "dash-period"
    DISCONTINUITY = "discontinuity"
    SCTE35_MARKER = "scte35-marker"
    DATERANGE = "daterange"
    HLS_MARKER = "hls-marker"
    DASH_EVENT = "dash-event"


class SignalEventType(Enum):
    CUE_IN = "cue-in"
    CUE_OUT = "cue-out"
    AD = "ad"
    SLATE = "slate"
    CONTENT = "content"


@dataclass
class LiveSignal:
    """Used to record signals that occur in the HLS/DASH manifests"""

    type: SignalType
    appeared_at: datetime
    content: object
    payload: object | None = None
    disappeared_at: datetime | None = None
    num_appearances: int = 0
    signal_event_type: SignalEventType | None = None
    signal_time: datetime | None = None  # The time that the signal applies to, eg. PDT

    @property
    def id(self):
        if self.payload:
            return (self.payload, self.signal_event_type, self.signal_time)
        if isinstance(self.content, m3u8.Segment):
            return (self.content.uri, self.content.current_program_date_time)


@dataclass
class Scte35Event:
    """Used to record SCTE35 events (as delimited by SCTE35 descriptors)"""

    event_id: int
    segment_type: scte35.Scte35DescriptorType
    occur: List[datetime] = field(default_factory=lambda: [])
    start: datetime | List[datetime] | None = None
    end: datetime | None = None
    duration: float | None = None
    upid: str | None = None
    upid_format: int | None = None
    position: int | None = None
    out_of: int | None = None
    chunks: List = field(default_factory=lambda: [])

    def relative_order_at_time(self, t: datetime):
        if self.end == self.start == t:
            return 0
        elif self.end == t:
            return -1
        elif self.start == t:
            return 2
        else:
            return 1

    def __hash__(self):
        return hash(self.event_id)


class LiveMonitor:
    def __init__(self) -> None:
        self.signals: dict = {}
        self.changes: dict = {}
        self.event_collector = Scte35EventCollector()
        self._timestamp: datetime

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.end()
        else:
            self.end()

    def __repr__(self):
        return f"<LiveMonitor signals={len(self.signals)} [A:{len(self.changes['added'])} U:{len(self.changes['updated'])} R:{len(self.changes['removed'])}]>"

    def _reset(self):
        self.changes = dict(
            added=[],
            updated=[],
            removed=[],
        )

    def start(self, timestamp: Optional[datetime] = None):
        # Start a new "transaction"
        self._reset()
        self._timestamp = timestamp or datetime.now()

    def end(self):
        # End the "transaction"

        # Search for removed signals
        signal: LiveSignal
        for sid, signal in self.signals.items():
            if not signal.disappeared_at:
                if (
                    signal not in self.changes["updated"]
                    and signal not in self.changes["added"]
                ):
                    self.changes["removed"].append(signal)
                    self.signals[signal.id].disappeared_at = self._timestamp

    def record_signal(self, signal: LiveSignal) -> LiveSignal:
        # previously seen signal
        if signal.id in self.signals:
            signal = self.signals[signal.id]
            self.changes["updated"].append(signal)

        # new signal
        else:
            signal.appeared_at = self._timestamp
            self.changes["added"].append(signal)

        # then increment count and overwrite
        signal.num_appearances += 1
        self.signals[signal.id] = signal

        # extract event information
        if signal.payload:
            self.record_scte35(signal.payload, signal.signal_time)

        return signal

    def record_scte35(self, payload: str, signal_time: datetime) -> Scte35Event:
        cue = Cue(payload)
        cue.decode()

        for d in cue.descriptors:
            self.event_collector.add_descriptor(d, signal_time)


class Scte35EventCollector:
    def __init__(self) -> None:
        self.events = {}

    def add_descriptor(self, descr: SegmentationDescriptor, signal_time: datetime):
        # find the segmentation type
        seg_type = scte35.get_descriptor_type(descr.segmentation_type_id)
        if not seg_type:
            return

        # search for an existing event
        event_id = int(descr.segmentation_event_id, 16)
        if event_id in self.events:
            event = self.events[event_id]
        else:
            event = Scte35Event(event_id=event_id, segment_type=seg_type)
            self.events[event_id] = event

        # populate it
        if not seg_type.pair:
            event.occur.append(signal_time)
        if seg_type.pair and descr.segmentation_type_id == seg_type.id:
            event.start = signal_time
        if seg_type.pair and descr.segmentation_type_id == seg_type.end_id:
            event.end = signal_time

        if descr.segmentation_duration:
            event.duration = descr.segmentation_duration
        if descr.segmentation_upid:
            if descr.segmentation_upid_type == 12:
                event.upid_format = descr.segmentation_upid["format_identifier"]
                event.upid = descr.segmentation_upid["private_data"]
            else:
                event.upid = descr.segmentation_upid
        if descr.segment_num:
            event.position = descr.segment_num
            event.out_of = descr.segments_expected

    def get_all_times(self) -> List[datetime]:
        times = set()
        for event in self.events.values():
            times.update(event.occur)

            if event.start:
                times.add(event.start)

            if event.end:
                times.add(event.end)
        return sorted(times)

    def get_events_for_time(self, t, boundaries_only=True) -> List[Scte35Event]:
        events = set()
        for event in self.events.values():
            if t in event.occur:
                events.add(event)

            if event.start == t:
                events.add(event)

            if event.end == t:
                events.add(event)

            if event.segment_type.pair and (
                (event.start and event.end and event.start < t and t < event.end)
                or (event.start and not event.end and event.start < t)
                or (event.end and not event.start and t < event.end)
            ):
                events.add(event)

        # sort them do that the end ones come first
        events = sorted(events, key=lambda e: e.relative_order_at_time(t))
        return list(events)

    def get_segmentation_types_used(self) -> List[scte35.Scte35DescriptorType]:
        types = set()
        for event in self.events.values():
            types.add(event.segment_type)

        sorted_types = sorted(types, key=lambda t: t.id)
        return sorted_types

    def get_first_event_of_type(
        self, st: scte35.Scte35DescriptorType
    ) -> Scte35Event | None:
        for t in self.get_all_times():
            events = self.get_events_for_time(t)

            # only keep the ones for that segmentation type
            typed_events = [e for e in events if e.segment_type == st]
            typed_events = sorted(
                typed_events, key=lambda e: e.relative_order_at_time(t)
            )
            if typed_events:
                return typed_events[0]

    def make_table(self):
        times = self.get_all_times()
        schedule = []

        max_box_size = 38

        for t in times:
            record = dict(time=str(t), ongoing={})
            events = self.get_events_for_time(t, boundaries_only=False)
            for e in events:
                color_line = functools.partial(
                    click.style, fg=e.segment_type.color(), bold=False
                )
                color_title = functools.partial(
                    click.style, bg=e.segment_type.color(), fg="white", bold=True
                )

                ongoing = None
                header = None
                body = []
                footer = None
                if e.start == t and e.end == t:
                    header = str(e.event_id)
                    footer = "(start & end)"
                    ongoing = False
                elif e.start == t:
                    # line1 = f"{e.event_id} (start)"
                    header = str(e.event_id)
                    ongoing = True
                elif e.end == t:
                    # line1 = f"{e.event_id} (end)"
                    footer = str(e.event_id)
                    ongoing = False
                elif t in e.occur:
                    header = str(e.event_id)
                    ongoing = False

                if e.start == t or t in e.occur:
                    if e.upid:
                        try:
                            upid_parsed = scte35.parse_mpu(e.upid_format, e.upid)
                            body.append(CL.labeled(upid_parsed["hex"], "u"))
                            # body.append(CL.labeled(upid_parsed["adBreakCode"], "code"))
                            # body.append(
                            #     CL.labeled(
                            #         upid_parsed["adBreakDuration"] / 1000,
                            #         "dur",
                            #         value_style=CL.high1,
                            #     )
                            # )
                        except Exception as error:
                            body.append(CL.labeled(e.upid, "upid"))

                if e.start == t or (not e.start and e.end == t):
                    if e.position:
                        body.append(
                            CL.labeled(
                                f"{e.position}/{e.out_of}", "seg", value_style=CL.attr
                            )
                        )
                    if e.duration:
                        body.append(CL.labeled(e.duration, "dur", value_style=CL.high1))

                # Colorize
                lines = []
                if header:
                    lines.append(
                        color_title(
                            trim_or_pad(f" {header} ", size=max_box_size, pad=True)
                        )
                    )
                if body:
                    line = " " + "  ".join([str(b) for b in body])
                    lines.append(
                        color_line("└" if not e.segment_type.pair else "│")
                        + trim_or_pad(line, size=max_box_size - 2, pad=True)
                        + color_line("╯" if not e.segment_type.pair else "│")
                    )

                if footer:
                    lines.append(
                        color_line(
                            "└"
                            + "─" * (max_box_size - 2 - len(footer) - 1)
                            + footer
                            + "─"
                            + "╯"
                        )
                    )

                cell = record.get(e.segment_type, [])
                if len(lines):
                    cell.append("\n".join(lines))
                record[e.segment_type] = cell

                # record if the column is ongoing
                record["ongoing"][e.segment_type] = ongoing

            schedule.append(record)

        # Prepare for tabulate (to re-order columns and pad the cells)
        headers = dict(time="time")
        for t in self.get_segmentation_types_used():
            headers[t] = str(t)

        ongoing_columns = {}
        # Seed them based on the segmentation type, and whether the first record in the column is an end one
        for t in self.get_segmentation_types_used():
            first_event_in_column = self.get_first_event_of_type(t)
            if (
                first_event_in_column
                and first_event_in_column.end
                and not first_event_in_column.start
            ):
                ongoing_columns[t] = True if t.pair else False

        table = []
        for record in schedule:
            max_lines = max_lines_in_dict(record)
            row: List[str] = []
            table.append(row)
            for h in headers.keys():
                # Determine if the row has has ongoing events in that column
                if isinstance(record["ongoing"].get(h), bool):
                    ongoing_columns[h] = record["ongoing"][h]
                if h in record and bool(record[h]):
                    if isinstance(record[h], list):
                        lines = record[h]
                        if ongoing_columns.get(h) is True:
                            lines = vertical_pad_table_cell(
                                lines, max_lines, h.color(), max_box_size
                            )
                        row.append("\n".join(lines))
                    else:
                        row.append(record[h])
                    # TODO - backfill to match max lines
                else:
                    if (
                        isinstance(h, scte35.Scte35DescriptorType)
                        and ongoing_columns.get(h) is True
                    ):
                        lines = vertical_pad_table_cell(
                            [], max_lines, h.color(), max_box_size
                        )

                        row.append("\n".join(lines))
                    else:
                        # single line to make it easier to find start time across columns
                        row.append(
                            # click.style(" " + "─" * (max_box_size - 2), fg="white", dim="true")
                            ""
                        )

        print(tabulate(table, headers=headers, tablefmt="psql"))
        return schedule


# Function to find the maximum number of lines in any string in the dictionary
def max_lines_in_dict(d):
    max_lines = 0
    for value_list in d.values():
        if isinstance(value_list, list):
            line_count = 0
            for s in value_list:
                line_count += s.count("\n") + 1
            if line_count > max_lines:
                max_lines = line_count
    return max_lines


def vertical_pad_table_cell(content, max_lines, color, witdh):
    line_count = 0
    if isinstance(content, list):
        for s in content:
            line_count += s.count("\n") + 1

    if line_count < max_lines:
        color_line = functools.partial(click.style, fg=color, bold=False)
        content.extend(
            [color_line("│") + " " * (witdh - 2) + color_line("│")]
            * (max_lines - line_count)
        )

    return content


def monitor_hls(
    handler: HLSHandler,
    max: int,
    interval: int,
    silent: bool,
    name: Optional[str] = None,
    save_to_file: bool = False,
    with_schedule: bool = False,
):
    # Go through the HLS document and retrieve segments with specific markers

    click.secho("Limitations:", fg="yellow")
    click.secho(
        "- this feature only monitors the first rendition in the multi-variant playlist",
        fg="yellow",
    )
    click.secho("- this feature will only work with specific SCTE markers", fg="yellow")
    print()

    bar = progressbar.ProgressBar(
        widgets=[
            CL.high1("---[ "),
            CL.node(name),
            CL.high1(" ]--[ "),
            progressbar.RotatingMarker(),
            CL.high1(" ]--[ "),
            progressbar.Counter(),
            CL.high1(" @ "),
            progressbar.Variable(name="time", format="{formatted_value}"),
            CL.high1(" ]--[ "),
            "HLS media sequence: ",
            progressbar.Variable(name="sequence", format="{value}"),
            CL.high1(" ]---"),
        ],
        redirect_stdout=True,
        max_value=progressbar.UnknownLength,
    )

    monitor = LiveMonitor()
    counter = max
    inc_counter = 0

    try:
        while True:
            stamp = datetime.now(timezone.utc)

            # Calculate datetimes for the whole span of the (sub-)manifest
            (start, end, duration, delta) = calculate_hls_pdt(handler, stamp)

            attrs = [
                CL.labeled(stamp.strftime("%H:%M:%S.%f"), "@", label_style=CL.high2),
                CL.labeled(handler.document.media_sequence, "seq"),
                CL.labeled(start, "start"),
                CL.labeled(duration, "len"),
                CL.labeled(end, "end"),
                CL.labeled(delta, "Δ", CL.high1),
            ]
            click.echo("  ".join(attrs))

            # Add to file
            if save_to_file:
                with open("monitor.txt", "a") as f:
                    f.write("  ".join(attrs) + "\n")
                    f.close()

            # Extract information from current HLS document
            changes = detect_hls_signals(handler, stamp, monitor)
            # print(monitor)
            if changes["added"]:
                if not silent:
                    sound_alert(changes["added"])

                # Print new ones
                for signal in changes["added"]:
                    line = "  ".join(
                        [
                            CL.alert("NEW"),
                            CL.labeled(signal.type.name, "type"),
                            CL.labeled(
                                (
                                    signal.signal_event_type.name
                                    if signal.signal_event_type
                                    else "-"
                                ),
                                "/",
                            ),
                            CL.labeled(
                                signal.signal_time.astimezone(timezone.utc).strftime(
                                    "%H:%M:%S"
                                ),
                                "for",
                            ),
                        ]
                    )
                    click.echo(line)
                    if signal.payload:
                        click.echo(CL.high3(signal.payload))
                        click.echo(("\n".join(summarize(signal.payload))))

                    click.echo(CL.expand(str(signal.content)))
                    click.echo()

                    # Add to file
                    if save_to_file:
                        with open("monitor.txt", "a") as f:
                            f.write(line + "\n")
                            f.write(str(signal.content) + "\n")
                            f.write("\n".join(summarize(signal.payload)) + "\n")
                            f.close()

                # Print a summary table
                if with_schedule:
                    monitor.event_collector.make_table()

            if counter == 1:
                break

            for j in range(4):
                time.sleep(int(interval) / 4)
                bar.update(
                    -counter - 1,
                    time=stamp.strftime("%H:%M:%S UTC"),
                    sequence=handler.document.media_sequence,
                )

            # time.sleep(int(interval))
            handler.reload()
            counter = counter - 1
            inc_counter = inc_counter + 1

    except KeyboardInterrupt:
        print("Stopped!")


def calculate_hls_pdt(handler: HLSHandler, now_stamp) -> Tuple[str, str, str, float]:
    start = handler.document.program_date_time
    end = handler.document.segments[-1].current_program_date_time
    end += timedelta(seconds=handler.document.segments[-1].duration)
    duration = end - start

    delta = end - now_stamp

    return (
        start.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f UTC"),
        end.astimezone(timezone.utc).strftime("%H:%M:%S.%f"),
        duration,
        delta.total_seconds(),
    )


def detect_hls_signals(handler: HLSHandler, stamp: datetime, monitor: LiveMonitor):
    with monitor as mon:
        # Detect markers
        for segment in handler.document.segments:
            # #EXT-X-DISCONTINUITY
            if segment.discontinuity:
                event_type = None
                if "/bpkio-jitt" in segment.uri:
                    event_type = SignalEventType.AD
                    if "/slate_" in segment.uri:
                        event_type = SignalEventType.SLATE

                mon.record_signal(
                    LiveSignal(
                        type=SignalType.DISCONTINUITY,
                        appeared_at=stamp,
                        content=segment,
                        signal_time=segment.current_program_date_time,
                        signal_event_type=event_type,
                    )
                )

            # #EXT-OATCLS-SCTE35
            if segment.oatcls_scte35:
                if segment.cue_out_start:
                    mon.record_signal(
                        LiveSignal(
                            type=SignalType.SCTE35_MARKER,
                            appeared_at=stamp,
                            content=segment,
                            signal_time=segment.current_program_date_time,
                            payload=segment.oatcls_scte35,
                            signal_event_type=SignalEventType.CUE_OUT,
                        )
                    )
                if segment.cue_in:
                    mon.record_signal(
                        LiveSignal(
                            type=SignalType.SCTE35_MARKER,
                            appeared_at=stamp,
                            content=segment,
                            signal_time=segment.current_program_date_time,
                            payload=segment.oatcls_scte35,
                            signal_event_type=SignalEventType.CUE_IN,
                        )
                    )

            # #EXT-X-DATERANGES
            for daterange in segment.dateranges:
                mon.record_signal(
                    LiveSignal(
                        type=SignalType.DATERANGE,
                        appeared_at=stamp,
                        content=segment,
                        signal_time=datetime.fromisoformat(
                            daterange.start_date.replace("Z", "+00:00")
                        )
                        if daterange.start_date
                        else stamp,
                        payload=(
                            daterange.scte35_out
                            or daterange.scte35_in
                            or daterange.scte35_cmd
                        ),
                        signal_event_type=(
                            SignalEventType.CUE_IN
                            if daterange.scte35_in
                            else SignalEventType.CUE_OUT
                        ),
                    )
                )

            # # Others
            # if segment.cue_in:
            #     mon.record_signal(
            #         LiveSignal(
            #             type=SignalType.SCTE35_MARKER,
            #             appeared_at=stamp,
            #             content=segment,
            #             signal_time=segment.current_program_date_time,
            #             signal_event_type=SignalEventType.CUE_IN,
            #             # payload=segment.scte35,
            #         )
            #     )

        return mon.changes


def sound_alert(signals: List[LiveSignal]):
    scte_signals = [
        s for s in signals if s.type in (SignalType.SCTE35_MARKER, SignalType.DATERANGE)
    ]
    if len(scte_signals):
        # only check the first signal
        if any(
            s for s in scte_signals if s.signal_event_type == SignalEventType.CUE_OUT
        ):
            sounds.chime_up()
        elif any(
            s for s in scte_signals if s.signal_event_type == SignalEventType.CUE_IN
        ):
            sounds.chime_down()
        else:
            sounds.chime()

    period_signals = [
        s for s in signals if s.type in (SignalType.DISCONTINUITY, SignalType.PERIOD)
    ]
    if len(period_signals):
        if any(s for s in period_signals if s.signal_event_type == SignalEventType.AD):
            sounds.chime_uphigh()
        else:
            sounds.chime()

    if any(s for s in signals if s not in scte_signals and s not in period_signals):
        sounds.chime()
