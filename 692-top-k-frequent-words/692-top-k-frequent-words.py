import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        alf = defaultdict(int)
        for word in words:
            alf[word] += 1
        h = []
        for key, val in alf.items():
            h.append([-val, key])
        h.sort()
        answer = []
        for i in range(k):
            answer.append(h[i][1])
        return answer