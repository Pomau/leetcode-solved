class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        main = set()
        open = defaultdict(int)
        close = defaultdict(int)
        for interval in intervals:
            open[interval[0]] += 1
            close[interval[1]] += 1
            main.add(interval[0])
            main.add(interval[1])
        events = sorted(list(main))
        now = 0
        for event in events:
            if now == 0 and open[event] > 0:
                answer.append([event])
            now += open[event]
            now -= close[event] 
            if now == 0:
                answer[-1].append(event)
        return answer
            
             
        