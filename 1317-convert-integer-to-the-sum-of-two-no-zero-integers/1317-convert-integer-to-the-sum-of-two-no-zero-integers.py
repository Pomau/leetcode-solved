class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            target = n - i
            if not self.check_zero(i) and not  self.check_zero(target):
                return [i, target]
        return [-1, -1]
    
    def check_zero(self, n):
        while n > 0:
            if n % 10 == 0:
                return True
            n //= 10
        return False