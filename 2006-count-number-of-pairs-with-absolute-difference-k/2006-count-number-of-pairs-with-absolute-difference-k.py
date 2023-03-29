class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        alf = defaultdict(int)
        ans = 0
        for l, el in enumerate(nums):
            for target in set([el - k, el + k]):
                ans += alf[target]
            alf[el] += 1
        return ans