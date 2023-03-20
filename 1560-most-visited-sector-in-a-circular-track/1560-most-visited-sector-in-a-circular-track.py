class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        places = [0] * n
        now = rounds[0] - 1
        places[now] += 1
        for i in range(1, len(rounds)):
            while now != rounds[i] - 1:
                now = (now + 1) % n
                places[now] += 1
        ans = []
        maxn = max(places)
        for i in range(n):
            if maxn == places[i]:
                ans.append(i + 1)
        return ans