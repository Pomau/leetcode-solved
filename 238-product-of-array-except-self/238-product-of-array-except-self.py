class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        for i in range(len(nums) - 1, -1, -1):
            answer.append(answer[-1] * nums[i])
        answer.reverse()
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix * answer[i + 1]
            prefix *= nums[i]
        answer.pop()
        return answer