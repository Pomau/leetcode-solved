class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.path = [[] for _ in range(numCourses)]
        self.color = [0] * numCourses # 0 не заходили 1 - зашли в нем 2 - вышли
        for from_node, to_node in prerequisites:
            self.path[from_node].append(to_node)
        for node in range(numCourses):
            if self.dfs(node):
                return False
        return True
    
    def dfs(self, u):
        haveCycle = False
        self.color[u] = 1
        for next_node in self.path[u]:
            if self.color[next_node] == 0:
                haveCycle = haveCycle or self.dfs(next_node)
            elif self.color[next_node] == 1:
                 haveCycle = True
        self.color[u] = 2
        return haveCycle
        
                
        