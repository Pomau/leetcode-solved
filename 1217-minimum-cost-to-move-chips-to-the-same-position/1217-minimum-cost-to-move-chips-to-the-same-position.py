class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ans = [0, 0]
        for i, pos in enumerate(position):
            ans[pos % 2] += 1
        return min(ans)