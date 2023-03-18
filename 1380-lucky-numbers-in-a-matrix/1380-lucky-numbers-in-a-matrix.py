class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mink = [float("inf")] * len(matrix)
        maxk = [float("-inf")] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mink[i] = min(mink[i], matrix[i][j])
                maxk[j] = max(maxk[j], matrix[i][j])
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == mink[i] == maxk[j]:
                    ans.append(matrix[i][j])
        return ans