class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        ch = True
        while n > 0:
            if ch and n % 2 == 1:
                ans[0] += 1
            elif not ch and n % 2 == 1:
                ans[1] += 1
            ch = not ch
            n //= 2
        return ans