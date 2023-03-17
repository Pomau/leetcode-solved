class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = [[arr[i], i] for i in range(len(arr))]
        nums.sort()
        ans = [0] * len(arr)
        last = float("-inf")
        rank = 0
        for i in range(len(nums)):
            if nums[i][0] != last:
                rank += 1
                last = nums[i][0]
            ans[nums[i][1]] = rank
        return ans