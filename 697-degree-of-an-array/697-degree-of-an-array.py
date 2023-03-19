class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        target = 0
        for num in nums:
            alf[num] += 1
            target = max(target, alf[num])
        now = float("inf")
        l = 0
        alf = defaultdict(int)
        for r in range(len(nums)):
            alf[nums[r]] += 1
            while alf[nums[r]] == target:
                now = min(now, r - l + 1)
                alf[nums[l]] -= 1
                l += 1
        return now
