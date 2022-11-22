class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        last = [-1, -1]
        for interval in sorted(intervals, key=lambda x: x[0]):
            if last[1] < interval[0]:
                answer.append(last)
                last = interval
            else:
                last[1] = max(last[1], interval[1])
        answer.append(last)
        return answer[1:]