class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        l = 0
        answer = []
        while r >= l:
            if abs(nums[r]) > abs(nums[l]):
                answer.append(nums[r]**2)
                r -= 1
            else:
                answer.append(nums[l]**2)
                l += 1
        answer.reverse()
        return answer