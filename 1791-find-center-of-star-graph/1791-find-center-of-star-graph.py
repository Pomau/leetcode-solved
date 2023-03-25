class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        variant = edges[0]
        for i in variant:
            if i not in edges[1]:
                variant.remove(i)
        return variant[0]