class MyDict:
    def __init__(self) -> None:
        self._dict: dict = {}

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def __len__(self):
        return len(self._dict)

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def pop(self, key, default=None):
        return self._dict.pop(key, default)

    def clear(self):
        self._dict.clear()

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()


# Without generics - no type hints for keys/values
untyped_dict = MyDict()
untyped_dict[123] = "hello"  # Works fine
untyped_dict["wrong"] = 456  # Also works, but could lead to bugs
untyped_dict[True] = [1, 2, 3]  # No consistency enforcement
