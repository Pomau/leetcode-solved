class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(
            self.f(distance, start, destination, 1),
            self.f(distance, start, destination, -1),
        )
    def f(self, dist, st, end, dx):
        ans = 0
        while st != end:
            target = (st + dx) % len(dist)
            if dx < 0:
                ans += dist[target]
            else:
                ans += dist[st]
            st = target
        return ans
            