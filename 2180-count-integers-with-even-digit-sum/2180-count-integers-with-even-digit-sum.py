class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            sums = 0
            while i > 0:
                sums += i % 10
                i //= 10
            if sums % 2 == 0:
                ans += 1
        return ans
            