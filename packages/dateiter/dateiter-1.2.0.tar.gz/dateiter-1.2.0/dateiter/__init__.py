import importlib.metadata
from datetime import date, datetime, timedelta
from typing import Any, Generator, assert_never

__version__ = importlib.metadata.version("dateiter")


DEFAULT_DATE_FORMAT = "%Y-%m-%d"


def dateiter(
    start: str | datetime | date,
    end: str | datetime | date | None,
    step: int = 1,
    format: str = DEFAULT_DATE_FORMAT,
) -> Generator[datetime, Any, None]:
    match start:
        case str():
            start_datetime = datetime.strptime(start, format)
        case date():
            start_datetime = datetime.combine(start, datetime.min.time())
        case datetime():
            start_datetime = start
        case _:
            assert_never(start)

    match end:
        case None:
            end_datetime = datetime.today()
        case str():
            end_datetime = datetime.strptime(end, format)
        case date():
            end_datetime = datetime.combine(end, datetime.min.time())
        case datetime():
            end_datetime = end
        case _:
            assert_never(end)

    while start_datetime < end_datetime:
        yield start_datetime
        start_datetime += timedelta(days=step)
