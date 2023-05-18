class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        alf = defaultdict(list)
        for edge in edges:
            alf[edge[1]].append(edge[0])
        for i in range(n):
            if len(alf[i]) == 0:
                ans.append(i)
        return ans