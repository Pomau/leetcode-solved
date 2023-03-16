class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        x = [0] * m
        y = [0] * n
        for indice in indices:
            x[indice[0]] += 1
            y[indice[1]] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if (x[i] + y[j]) % 2 == 1:
                    ans += 1
        return ans