class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        alf = defaultdict(list)
        ans = 0
        for i in range(len(grid)):
            hash_l = 0
            for j in range(len(grid[i])):
                hash_l = hash_l * 31 + grid[i][j]
            alf[hash_l].append(i)
        for i in range(len(grid)):
            hash_l = 0
            for j in range(len(grid)):
                hash_l = hash_l * 31 + grid[j][i]
            for c in alf[hash_l]:
                os = True
                for k in range(len(grid)):
                    if grid[c][k] != grid[k][i]:
                        os = False
                if os:
                    ans += 1
        return ans
                    