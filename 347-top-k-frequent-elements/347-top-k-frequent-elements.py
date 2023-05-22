class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        alf = defaultdict(int)
        for num in nums:
            alf[num] += 1
        h = []
        for key, val in alf.items():
            heapq.heappush(h, [val, key])
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        while len(h) > 0:
            ans.append(heapq.heappop(h)[1])
        return ans