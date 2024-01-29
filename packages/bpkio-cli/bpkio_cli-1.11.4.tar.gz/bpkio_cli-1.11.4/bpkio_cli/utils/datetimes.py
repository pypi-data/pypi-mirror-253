from datetime import datetime, timedelta
from typing import Optional

import arrow
import dateparser
import pytimeparse
import pytz
from tzlocal import get_localzone


def parse_date_string(date: str) -> float:
    return dateparser.parse(date).timestamp()


def get_utc_date_ranges(
    from_time: datetime, to_time: Optional[datetime] = None, unit: str = "month"
):
    if to_time:
        end = arrow.get(to_time)
    else:
        end = arrow.utcnow()

    start = arrow.get(from_time).replace(hour=0, minute=0, second=0, microsecond=0)

    range = arrow.Arrow.span_range(unit, start=start, end=end, exact=True)  # type: ignore

    return [(s.datetime, e.datetime) for (s, e) in range]


def parse_date_expression_as_utc(exp: str | tuple | list, future=True) -> datetime:
    if isinstance(exp, (tuple, list)):
        exp = " ".join(exp)

    # If a number, it's seconds in the future
    if exp.isnumeric():
        if future:
            return datetime.utcnow() + timedelta(seconds=float(exp))
        else:
            return datetime.utcnow() - timedelta(seconds=float(exp))

    else:
        current_tz_name = str(get_localzone())

        # Parse the input string into a datetime object considering the timezone information
        dt_local = dateparser.parse(
            exp,
            settings={
                "TIMEZONE": current_tz_name,
                "RETURN_AS_TIMEZONE_AWARE": True,
                "PREFER_DATES_FROM": "future" if future else "past",
            },
        )

        # Convert the datetime object to UTC timezone
        dt_utc = dt_local.replace(microsecond=0).astimezone(pytz.UTC)

        return dt_utc


def parse_duration_expression(exp: str | tuple | list) -> float:
    if isinstance(exp, (tuple, list)):
        exp = " ".join(exp)

    try:
        return float(exp)
    except ValueError:
        return pytimeparse.parse(exp)


def seconds_to_timecode(duration: float, with_milliseconds=False) -> str:
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)

    if with_milliseconds:
        return f"{int(hours)}:{int(minutes):02d}:{seconds:02d}.{milliseconds:03d}"
    else:
        return f"{int(hours)}:{int(minutes):02d}:{seconds:02d}"
