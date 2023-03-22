class OrderedStream:

    def __init__(self, n: int):
        self.l = 0
        self.words = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.words[idKey - 1] = value
        ans = []
        while self.l < len(self.words) and self.words[self.l] != "":
            ans.append(self.words[self.l])
            self.l += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)