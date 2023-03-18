class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        time = timeSeries[0]
        for l, ser in enumerate(timeSeries):
            ans += (ser + duration - max(ser, time))
            time = ser + duration
        return ans