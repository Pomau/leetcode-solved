class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = [float("-inf") for _ in range(len(grid[0]))]
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                ans[i] = max(ans[i], len(str(grid[j][i])))
        return ans