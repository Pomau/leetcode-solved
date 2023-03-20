class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
        k = 0
        while n > 0:
            ans.append(str(n % 10))
            k += 1
            if k % 3 == 0 and n // 10 > 0:
                ans.append(".")
            n //= 10
        return "".join(reversed(ans))