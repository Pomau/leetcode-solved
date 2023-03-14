class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        for i, num in enumerate(nums):
            alf[num] += 1
            if alf[num] == len(nums)// 2:
                return num
        return -1