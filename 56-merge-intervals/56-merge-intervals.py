class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if len(answer) > 0 and answer[-1][1] >= interval[0]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer.append(interval)
        return answer
             
        