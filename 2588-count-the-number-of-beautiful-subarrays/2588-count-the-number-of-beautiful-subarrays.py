class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        ans = 0
        xor = 0
        alf[0] += 1
        for i in range(len(nums)):
            xor ^= nums[i]
            ans += alf[xor]
            alf[xor] += 1
        return ans