class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        l = 0
        r = 0
        while l < len(nums):
            answer.append(str(nums[l]))
            r = l + 1
            while r < len(nums) and nums[r] - 1 == nums[r - 1]:
                r += 1
            if r - 1 != l:
                answer[-1] += f"->{nums[r - 1]}"
            l = r
        return answer