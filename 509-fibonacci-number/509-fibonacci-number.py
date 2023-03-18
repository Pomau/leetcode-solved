class Solution:
    def fib(self, n: int) -> int:
        last = 0
        next = 1
        for i in range(n):
            next, last = next + last, next
        return last