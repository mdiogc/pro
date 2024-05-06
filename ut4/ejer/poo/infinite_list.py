class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.items = list(args)
        self._fill_value = fill_value

    def _extend_list(self, index):
        self.items.extend([self._fill_value] * (index - len(self.items) + 1))

    def __getitem__(self, index: int):
        if index >= len(self.items):
            self._extend_list(index)
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __setitem__(self, index: int, item) -> None:
        if index >= len(self.items):
            self._extend_list(index)
        self.items[index] = item

    def __str__(self):
        return ','.join(str(x) for x in self.items if x is not None)
