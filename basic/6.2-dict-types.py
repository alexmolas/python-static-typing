class MyDict[K, V]:
    def __init__(self) -> None:
        self._dict: dict[K, V] = {}

    def __getitem__(self, key: K) -> V:
        return self._dict[key]

    def __setitem__(self, key: K, value: V) -> None:
        self._dict[key] = value

    def __delitem__(self, key: K) -> None:
        del self._dict[key]

    def __contains__(self, key: K) -> bool:
        return key in self._dict

    def __len__(self) -> int:
        return len(self._dict)

    def get(self, key: K, default=None) -> V | None:
        return self._dict.get(key, default)

    def pop(self, key: K, default=None) -> V | None:
        return self._dict.pop(key, default)

    def clear(self):
        self._dict.clear()

    def keys(self) -> list[K]:
        return list(self._dict.keys())

    def values(self) -> list[V]:
        return list(self._dict.values())

    def items(self) -> list[tuple[K, V]]:
        return list(self._dict.items())


# With generics - explicit types for keys/values
user_scores: MyDict[str, int] = MyDict()
user_scores["alice"] = 100  # OK
user_scores["bob"] = 95  # OK
user_scores[123] = 80  # Type error: key must be str
user_scores["carol"] = "A+"  # Type error: value must be int
