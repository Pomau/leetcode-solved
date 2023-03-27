class Solution:
    def isThree(self, n: int) -> bool:
        ans = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                ans += 1
                if n // i != i:
                    ans += 1
        return ans == 3