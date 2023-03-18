class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n > 1:
            n //= 3
        if n != 1:
            return False
        return True
        