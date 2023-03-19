class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if self.check(i):
                ans.append(i)
        return ans

    def check(self, x):
        num = x
        while num >= 1:
            now = num  % 10
            if now == 0 or x % now != 0:
                return False
            num //= 10
        return True