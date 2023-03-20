class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            ans += alf[num]
            alf[num] += 1
        return ans