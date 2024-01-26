import datetime
import typing
import dataclasses


@dataclasses.dataclass()
class Postpone:
    
    date: datetime.date
    reason: str


class DateIterator:

    def __init__(
        self,
        start: datetime.date,
        end: datetime.date,
        closable: bool,
        order_dates: typing.List[datetime.date],
        allow_weekends=False,
        allow_holidays=False
    ):
        self.start = start
        self.end = end
        self.closable = closable
        self.order_dates = order_dates
        self.allow_weekends = allow_weekends
        self.allow_holidays = allow_holidays
        self.postponned = []

        self._date = None

    def __iter__(self):
        if self.start is None:
            return iter([])

        if self._date is not None:
            raise ValueError("double iter")

        self._date = self.start
        return self

    def _should_skip_weekends(
        self,
        date: datetime.date,
        ordered: bool,
        postponned: typing.List[Postpone]
    ) -> bool:
        if self.allow_weekends or date.weekday() <= 4:
            return False

        if ordered:
            postponned.append(Postpone(
                date,
                "weekend"
            ))

        return True

    def _should_skip_holidays(
        self,
        date: datetime.date,
        ordered: bool,
        postponned: typing.List[Postpone]
    ) -> bool:
        from .data.holidays import holidays as days
        
        if self.allow_holidays or date not in days:
            return False

        if ordered:
            postponned.append(Postpone(
                date,
                "holiday"
            ))

        return True

    def __next__(self):
        postponned: typing.List[Postpone] = []

        while self._date <= self.end:
            date = self._date
            self._date += datetime.timedelta(days=1)

            ordered = date in self.order_dates

            if self.closable:
                if self._should_skip_weekends(date, ordered, postponned):
                    continue

                if self._should_skip_holidays(date, ordered, postponned):
                    continue

            return date, ordered, postponned

        raise StopIteration
