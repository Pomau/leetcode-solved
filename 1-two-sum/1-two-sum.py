class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = defaultdict(int)
        for i in range(len(nums)):
            second = target - nums[i]
            if second in numbers:
                return [i, numbers[second]]
            numbers[nums[i]] = i