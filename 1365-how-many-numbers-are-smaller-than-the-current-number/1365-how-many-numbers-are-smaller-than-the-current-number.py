class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [[nums[i], i] for i in range(len(nums))]
        ans = [0] * len(nums)
        arr.sort()
        k = 0
        for i in range(len(arr)):
            if i > 0 and arr[i][0] != arr[i - 1][0]:
                k = i
            ans[arr[i][1]] = k
        return ans