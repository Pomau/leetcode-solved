class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = [[[] for j in range(2)] for i in range(n)]
        for road in connections:
            roads[road[0]][1].append(road[1])
            roads[road[1]][0].append(road[0])
        ans = 0
        q = [(0, -1)]
        l = 0
        while len(q) > l:
            node, last = q[l]
            l += 1
            for road in roads[node][0]:
                if road == last:
                    continue
                q.append((road, node))
            for road in roads[node][1]:
                if road == last:
                    continue
                q.append((road, node))
                ans += 1
        return ans