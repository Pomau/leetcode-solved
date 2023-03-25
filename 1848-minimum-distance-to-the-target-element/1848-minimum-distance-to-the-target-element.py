class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float("inf")
        for i in range(len(nums)):
            if nums[i] == target and abs(i - start) < ans:
                ans = abs(i - start)
        return ans