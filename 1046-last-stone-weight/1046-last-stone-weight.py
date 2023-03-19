import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones) * -1
            max2 = heapq.heappop(stones) * -1
            if max1 != max2:
                heapq.heappush(stones, (max1-max2) *-1)
        if len(stones) == 0:
            return 0
        return heapq.heappop(stones) *-1