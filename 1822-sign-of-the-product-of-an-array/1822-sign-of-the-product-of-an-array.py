class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for el in nums:
            result *= el
        if result > 0:
            result = 1
        elif result == 0:
            result = 0
        else:
            result = -1
        return result