class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [[mat[i], i] for i in range(len(mat))]
        arr.sort(key=lambda x: [x[0].count(1), x[1]])
        return [arr[i][1] for i in range(k)]