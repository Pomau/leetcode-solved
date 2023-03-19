class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n % 2
        n //= 2
        while n > 0:
            if last == n % 2:
                return False
            last = n % 2
            n //= 2
        return True