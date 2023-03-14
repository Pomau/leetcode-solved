class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [[0, 0] for i in range(n)]
        for i in range(len(trust)):
            a[trust[i][0] - 1][0] += 1
            a[trust[i][1] - 1][1] += 1
        for i in range(n):
            if a[i][0] == 0 and a[i][1] == n - 1:
                return i + 1
        return -1