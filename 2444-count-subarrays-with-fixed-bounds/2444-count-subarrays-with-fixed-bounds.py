class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minF = False
        maxF = False
        ans = 0
        min_i = -1
        max_i = -1
        st = 0
        for r, el in enumerate(nums):
            if el < minK or el > maxK:
                st = r + 1
                minF = False
                maxF = False
            if el == minK:
                minF = True
                min_i = r
            if el == maxK:
                maxF = True
                max_i = r
            if minF and maxF:
                ans += (min(min_i, max_i) - st + 1)
        return ans