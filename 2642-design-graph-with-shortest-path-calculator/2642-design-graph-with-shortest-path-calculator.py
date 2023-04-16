class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.path = defaultdict(list)
        for edge in edges:
            self.path[edge[0]].append([edge[1], edge[2]])
        

    def addEdge(self, edge: List[int]) -> None:
        self.path[edge[0]].append([edge[1], edge[2]])
        

    def shortestPath(self, node1: int, node2: int) -> int:
        q = []
        heapq.heappush(q, [0, node1])
        color = set()
        # print(self.path)
        while len(q) > 0:
            # print(q, node1, node2)
            arr = heapq.heappop(q)
            node = arr[1]
            cost = arr[0]
            if node in color:
                continue
            color.add(node)
            if node == node2:
                return cost
            for edge in self.path[node]:
                heapq.heappush(q, [cost + edge[1], edge[0]])
        return -1
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)