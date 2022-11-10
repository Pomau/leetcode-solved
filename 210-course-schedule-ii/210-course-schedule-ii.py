class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.path = [[] for _ in range(numCourses)]
        self.color = [0] * numCourses
        self.answer = []
        for way in prerequisites:
            self.path[way[0]].append(way[1])
        for node in range(numCourses):
            if self.color[node] == 0 and self.dfs(node):
                self.answer = []
                break
        return self.answer

    def dfs(self, node):
        self.color[node] = 1
        hasCycle = False
        for next_node in self.path[node]:
            if self.color[next_node] == 1:
                hasCycle = True
            elif self.color[next_node] == 0:
                hasCycle = hasCycle or self.dfs(next_node)
        self.color[node] = 2
        self.answer.append(node)
        return hasCycle
    
    # 1 -> 0
    # 2 -> 0
    # 3 -> 1 
    # 3 -> 2