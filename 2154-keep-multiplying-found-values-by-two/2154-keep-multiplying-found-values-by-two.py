class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        target = original
        alf = set(nums)
        while target in alf:
            target *= 2
        return target