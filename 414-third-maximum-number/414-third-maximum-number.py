class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        answer = []
        for num in nums:
            if num not in answer:
                answer.append(num)
                l = len(answer) - 1
                while l > 0 and answer[l] > answer[l - 1]:
                    answer[l], answer[l-1] = answer[l - 1], answer[l]
                    l -= 1
                if len(answer) == 4:
                    answer.pop()
        if len(answer) == 3:
            return answer[-1]
        return answer[0]