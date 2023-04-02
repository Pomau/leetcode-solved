class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        alf = defaultdict(int)
        best = 0
        for i, el in enumerate(nums):
            if el == key and i + 1 < len(nums):
                alf[nums[i + 1]] += 1
                best = nums[i + 1]
        for key, val in alf.items():
            if val > alf[best]:
                best = key
        return best