class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nch = 0
        ch = 0
        for l in range(len(nums)):
            if l % 2 == 0:
                while nums[ch] % 2 == 1:
                    ch += 1
                nums[l], nums[ch] = nums[ch], nums[l]
                ch += 1
            else:
                while nums[nch] % 2 == 0:
                    nch += 1
                nums[l], nums[nch] = nums[nch], nums[l]
                nch += 1
        return nums