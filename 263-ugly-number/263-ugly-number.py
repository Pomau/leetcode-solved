class Solution:
    def isUgly(self, n: int) -> bool:
        ugly = [2, 3, 5]
        for k in ugly:
            otv = 1
            while n > otv:
                otv *= k
            while otv > 1:
                if n % otv == 0:
                    n = n // otv
                else:
                    otv /= k
        return 0 < n <= 1 