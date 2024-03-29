class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            k = min(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
            ans += k
            ans += abs(abs(points[i][0] - points[i - 1][0]) - k) +  abs(abs(points[i][1] - points[i - 1][1]) - k)
        return ans 