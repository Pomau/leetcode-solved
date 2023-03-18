class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.k = 0

    def visit(self, url: str) -> None:
        while self.k != len(self.arr) - 1:
            self.arr.pop()
        self.arr.append(url)
        self.k += 1

    def back(self, steps: int) -> str:
        self.k = max(self.k - steps, 0)
        return self.arr[self.k]
        

    def forward(self, steps: int) -> str:
        self.k = min(self.k + steps, len(self.arr) - 1)
        return self.arr[self.k]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)