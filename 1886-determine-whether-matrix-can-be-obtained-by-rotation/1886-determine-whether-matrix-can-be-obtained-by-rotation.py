class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for k in range(4):
            mat = self.newMat(mat)
            os = True
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] != target[i][j]:
                      os = False
            if os:
                return True
        return False
    def newMat(self, mat):
        ans = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[j][len(mat) - i-1] = mat[i][j]
        return ans