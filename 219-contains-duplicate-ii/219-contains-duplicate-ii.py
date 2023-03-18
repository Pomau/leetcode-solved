class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        alf = defaultdict(int)
        for r, ch in enumerate(nums):
            alf[ch] += 1
            if r > k:
                alf[nums[r - k - 1]] -= 1
            if alf[ch] > 1:
                return True
        return False