class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        small = -1
        for l, point in enumerate(points):
            if x != point[0] and y != point[1]:
                continue
            if small == -1 or self.distance(points[small], [x, y]) > self.distance(point, [x, y]):
                small = l
        return small
    def distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
