class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = max(time) * totalTrips
        while r - l > 1:
            m = (r + l) // 2
            if self.check(time, m) >= totalTrips:
                r = m
            else:
                l = m
        return r
    
    def check(self, times, target):
        answer = 0
        for time in times:
            answer += target // time
        return answer