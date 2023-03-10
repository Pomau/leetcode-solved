class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        answer = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for z in range(j + 1, len(points)):
                    answer = max(answer, self.eval(points[i], points[j], points[z]))
        return answer
    def eval(self, p1, p2, p3):
        return 0.5 * abs((p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1]))