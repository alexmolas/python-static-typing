from typing import overload


@overload
def add(x: int, y: int) -> int: ...


@overload
def add(x: str, y: str) -> str: ...


def add(x: int | str, y: int | str) -> int | str:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    else:
        raise TypeError("Arguments must be both integers or both strings")


add(1, 1)
add("a", "b")
add("a", 1)
