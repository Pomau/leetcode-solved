class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                c = int(sqrt(i ** 2 + j ** 2))
                if c ** 2 == i ** 2 + j ** 2 and 1 <= c <= n:
                    ans += 1
                    if i != j:
                        ans += 1
        return ans