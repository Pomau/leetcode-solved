class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        now = 0
        for i in range(len(nums)):
            now = (now * 2 + nums[i]) % 5
            answer.append(now == 0)
        return answer