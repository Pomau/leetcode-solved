class Solution:
    def findLHS(self, nums: List[int]) -> int:
        alf = defaultdict(int)
        ans = 0
        for num in nums:
            alf[num] += 1
        for key, item in alf.items():
            now = 0
            if key + 1 in alf:
                now += alf[key + 1] + item
            ans = max(ans, now)
        return ans