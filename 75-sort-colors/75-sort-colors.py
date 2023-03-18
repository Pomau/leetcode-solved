class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for i in nums:
            colors[i] += 1
        color_id = 0
        nums_id = 0
        while color_id < 3:
            if colors[color_id] <= 0:
                color_id += 1
                continue
            nums[nums_id] = color_id
            colors[color_id] -= 1
            nums_id += 1