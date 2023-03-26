class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            ind = 0
            target = nums[i]
            if i > 0:
                target -= nums[i - 1]
            prostoe = target - 1
            while prostoe > 1:
                os = True
                for j in range(2, int(sqrt(prostoe)) + 1):
                    if prostoe % j == 0:
                        os = False
                        break
                if os:
                    break
                prostoe -= 1
            if prostoe > 1:
                nums[i] -= prostoe
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True