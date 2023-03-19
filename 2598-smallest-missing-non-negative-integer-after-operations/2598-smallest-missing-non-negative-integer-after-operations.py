class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        alf = defaultdict(int)
        for num in nums:
            alf[num % value] += 1
        target = 0
        while True:
            if alf[target % value] <= 0:
                return target
            alf[target % value] -= 1
            target += 1
        return -1