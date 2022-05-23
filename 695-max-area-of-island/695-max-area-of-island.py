class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n, visit, area, ma = len(grid), len(grid[0]), set(), 0, 0
        
        def dfs(r, c):
            nonlocal area, ma
            if r<m and c<n and r>=0 and c>=0 and grid[r][c] == 1 and (r,c) not in visit:
                
                area += 1
                ma = max(ma, area)
                print(area, ma)
                visit.add((r,c))
            else:
                return
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    area = 0
                    dfs(i, j)
                    
        return ma