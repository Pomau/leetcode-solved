class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        roads = defaultdict(list)
        for edge in edges:
            roads[edge[0]].append(edge[1])
            roads[edge[1]].append(edge[0])
        ans = float("inf")
        for i in range(n):
            color = [-1]* n
            q = deque()
            q.append([i, 0, -1])
            while len(q) > 0:
                u, s, last = q.popleft()
                #print(u, s, last, "----------------")
                if color[u] != -1:
                    continue
                color[u] = s
                for road in roads[u]:
                    if road == last:
                        continue
                    if color[road] != -1:
                        #print(u, road, color[road] + s +1)
                        ans = min(ans, color[road] + s +1)
                        continue
                    q.append([road, s + 1, u])
        if ans == float("inf"):
            ans = -1
        return ans
            
            