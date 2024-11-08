from dataclasses import dataclass
from datetime import datetime
from typing import Any, Protocol, Self, runtime_checkable


@dataclass
class Increment[Time]:
    id: str
    time: Time

    def description(self: Self) -> str:
        return "Incremented counter"


@dataclass
class Reset[Time]:
    id: str
    time: Time

    def description(self: Self) -> str:
        return "Reset counter"


@runtime_checkable
class Event[Time](Protocol):
    id: str
    time: Time

    def description(self: Self) -> str: ...


def log_event(event: Event[datetime]):
    print(f"Got {event.id} at {event.time}: {event.description()}")


def log(x: Any):
    match x:
        case Event() if isinstance(datetime, x.time):
            log_event(x)
        case _:
            print(x)


log(
    Increment("foo", datetime.now()),
)
