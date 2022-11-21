class RecentCounter:

    def __init__(self):
        self.arr = []
        self.l = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while t - self.arr[self.l] > 3000:
            self.l += 1
        return len(self.arr) - self.l
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)