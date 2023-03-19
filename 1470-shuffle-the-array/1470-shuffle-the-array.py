class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for l in range(n):
            ans += [nums[l], nums[n + l]]
        return ans