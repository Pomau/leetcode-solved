class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxn = 0
        ans = 0
        years = [[log[0], 1] for log in logs] + [[log[1], -1] for log in logs]
        years.sort()
        now = 0
        for i in range(len(years)):
            now += years[i][1]
            if now > maxn:
                maxn = now
                ans = years[i][0]
        return ans