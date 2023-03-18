class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] >= 0:
                number = nums[i] - 1
                if number < len(nums) and nums[number] > 0:
                    nums[i] = nums[number]
                    nums[number] = -1
                else:
                    break
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                answer.append(i + 1)
        return answer
                
        