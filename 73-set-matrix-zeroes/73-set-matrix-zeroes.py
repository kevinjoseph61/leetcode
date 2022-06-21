class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r, c = [False] * m, [False] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r[i], c[j] = True, True
        
        for i in range(m):
            for j in range(n):
                if r[i] or c[j]:
                    matrix[i][j] = 0 