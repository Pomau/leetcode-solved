class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        alf = defaultdict(int)
        for num in nums:
            alf[num] += 1
        for key, val in alf.items():
            if val % 2 == 1:
                return False
        return True