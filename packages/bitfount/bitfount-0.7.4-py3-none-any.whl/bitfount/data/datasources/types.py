"""Datasource related types."""
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, TypedDict

from typing_extensions import NotRequired


@dataclass
class Date:
    """Simple date class used for filtering files based on date headers.

    This is used by `FileSystemIterableSource` to filter files based on
    their creation and modification dates.

    Args:
        year: The oldest possible year to consider.
        month: The oldest possible month to consider. If None, all months
            in the given year are considered. Defaults to None.
        day: The oldest possible day to consider. If None, all days in the
            given month are considered. If month is None, this is ignored.
            Defaults to None.
    """

    year: int
    month: Optional[int] = None
    day: Optional[int] = None

    def get_date(self) -> date:
        """Get a datetime.date object from the date components year, month and day."""
        if self.month:
            if self.day:
                cutoff_datetime = datetime(self.year, self.month, self.day)
            else:
                cutoff_datetime = datetime(self.year, self.month, 1)
        else:
            cutoff_datetime = datetime(self.year, 1, 1)

        return cutoff_datetime.date()


class DateTD(TypedDict):
    """Typed dict form of Date dataclass."""

    year: int
    month: NotRequired[int]
    day: NotRequired[int]
