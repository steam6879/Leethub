class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict

        self.dict = OrderedDict()
        self.capa = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value

        if len(self.dict) > self.capa:
            self.dict.popitem(last=False)