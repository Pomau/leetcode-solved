class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxn = max(nums)
        minn = min(nums)
        return self.gcd(maxn, minn)
    
    def gcd(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b