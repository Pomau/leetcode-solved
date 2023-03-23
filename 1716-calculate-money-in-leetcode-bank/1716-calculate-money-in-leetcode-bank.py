class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        ans = (28 + (21 + (7 * week))) * week // 2
        n -= week * 7
        for i in range(n):
            ans += ((i + 1) + week * 1)
        return ans