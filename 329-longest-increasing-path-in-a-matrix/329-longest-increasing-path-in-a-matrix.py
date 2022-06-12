class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        Gma = 0
        
        @functools.cache
        def dfs(i, j):
            nonlocal Gma
            
            m1, m2, m3, m4 = 0, 0, 0, 0
            x, y = i+1, j
            if x>=0 and y>=0 and x<m and y<n and matrix[x][y]>matrix[i][j]:
                m1 = dfs(x, y) + 1
            x, y = i, j+1
            if x>=0 and y>=0 and x<m and y<n and matrix[x][y]>matrix[i][j]:
                m2 = dfs(x, y) + 1
            x, y = i-1, j
            if x>=0 and y>=0 and x<m and y<n and matrix[x][y]>matrix[i][j]:
                m3 = dfs(x, y) + 1
            x, y = i, j-1
            if x>=0 and y>=0 and x<m and y<n and matrix[x][y]>matrix[i][j]:
                m4 = dfs(x, y) + 1
            
            Lma = max(m1, m2, m3, m4)
            Gma = max(Lma, Gma)
            
            #print(Lma, Gma)
            
            return Lma
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        return Gma + 1
            