class MyHashSet:

    def __init__(self):
        self.myHash = set()

    def add(self, key: int) -> None:
        if key not in self.myHash:
            self.myHash.add(key)

    def remove(self, key: int) -> None:
        if key in self.myHash:
            self.myHash.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.myHash

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)