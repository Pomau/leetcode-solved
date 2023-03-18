class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        answer = []
        r = len(nums) - (k % len(nums))
        for i in range(r, len(nums)):
            answer.append(nums[i])
        for i in range(0, r):
            answer.append(nums[i])
        for i in range(len(nums)):
            nums[i] = answer[i]