class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:

        n = len(mat)

        for k in range(4):

            matrix2 = [[0] * n for i in range(n)]

            for i in range(n):
                for j in range(n):
                    matrix2[j][n-i-1] = mat[i][j]

            mat = matrix2

            if mat == target:
                return True

        return mat == target or mat == target