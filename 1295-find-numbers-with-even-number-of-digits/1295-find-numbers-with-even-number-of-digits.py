class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            now = 0
            while num > 0:
                num //= 10
                now += 1
            if now % 2 == 0:
                ans += 1
        return ans