class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        sums = 0
        for height in gain:
            sums += height
            ans = max(sums, ans)
        return ans