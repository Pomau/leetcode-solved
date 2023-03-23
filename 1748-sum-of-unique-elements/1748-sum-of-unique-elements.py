class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        for num in nums:
            alf[num] += 1
        ans = 0
        for key, item in alf.items():
            if item == 1:
                ans += key
        return ans