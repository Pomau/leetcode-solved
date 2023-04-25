class SmallestInfiniteSet:

    def __init__(self):
        self.b = set()

    def popSmallest(self) -> int:
        n = 1
        while n in self.b:
            n += 1
        self.b.add(n)
        return n
        

    def addBack(self, num: int) -> None:
        if num in self.b:
            self.b.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)