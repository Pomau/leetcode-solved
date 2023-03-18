class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[i] > 0:
                number = nums[i] - 1
                if nums[number] > 0:
                    nums[i] = nums[number]
                    nums[number] = -1
                else:
                    if nums[number] != 0:
                        res.append(number + 1)
                        nums[number] = 0
                    break
        return res
        