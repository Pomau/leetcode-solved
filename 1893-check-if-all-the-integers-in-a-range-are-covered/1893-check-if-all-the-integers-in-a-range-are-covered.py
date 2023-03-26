class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        intervals = [[x[0], 1] for x in ranges] + [[x[1] + 1, -1] for x in ranges] + [[left, 0], [right, 0]]
        ans = 0
        now = 0
        intervals.sort()
        for i in range(len(intervals)):
            now += intervals[i][1]
            if i + 1 < len(intervals) and intervals[i + 1][0] == intervals[i][0]:
                continue
            if now == 0 and left <= intervals[i][0] <= right:
                return False
        return True