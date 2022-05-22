class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n, visit, islands = len(grid), len(grid[0]), set(), 0
        
        def dfs(r, c):
            if r<m and c<n and r>=0 and c>=0 and grid[r][c]=="1" and (r,c) not in visit:
                visit.add((r,c))
            else:
                return
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    islands += 1
        return islands