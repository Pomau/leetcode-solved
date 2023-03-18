class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        alf = defaultdict(int)
        for num in nums:
            alf[num] += 1
            if alf[num] > 1:
                return True
        return False