class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        l = 0
        for r in range(1, len(nums) + 1):
            if len(nums) == r or nums[r] != nums[r - 1] + 1:
                answer.append(str(nums[l]))
                if r - l > 1:
                    answer[-1] += "->" + str(nums[r - 1])
                if len(nums) != r:
                    word = str(nums[r])
                l = r
        return answer