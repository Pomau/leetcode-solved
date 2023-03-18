class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for a in range(len(nums)):
            b = a + 1
            c = len(nums) - 1
            if nums[a] == nums[a-1] and a > 0:
                continue
            while c > b:
                sums = nums[a] + nums[b] + nums[c]
                if sums == 0:
                    res.append([nums[a], nums[b], nums[c]])
                if sums > 0:
                    c -= 1
                else:
                    b += 1
                    while(nums[b] == nums[b-1] and c > b):
                        b += 1
        return res
        