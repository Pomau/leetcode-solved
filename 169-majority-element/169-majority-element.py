class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = -1
        for num in nums:
            if num != element:
                count -= 1
            else:
                count += 1
            if count < 0:
                count  = 1
                element = num
        return element