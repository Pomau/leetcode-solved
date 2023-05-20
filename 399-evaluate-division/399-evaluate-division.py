class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        for i, (var1, var2) in enumerate(equations):
            graph[var1].append((var2, values[i]))
            graph[var2].append((var1, 1.0 / values[i]))
            
        res = []
        
        def dfs(node, res):
            if node == end:
                return res
            visited.add(node)
            for neigh, val in graph[node]:
                if neigh not in visited:
                    score = dfs(neigh, res * val)
                    if score != -1:
                        return score
            return -1
                    
        for start, end in queries:
            visited = set([])
            if start not in graph or end not in graph:
                res.append(-1)
            else:
                res.append(dfs(start, 1))
        
        return res