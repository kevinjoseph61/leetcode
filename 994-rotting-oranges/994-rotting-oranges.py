class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, m, n, fresh, t = deque(), len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append(((i, j), 0))
        pos = [(0,1), (1, 0), (-1, 0), (0, -1)]
        while(q):
            (i, j), minute = q.popleft()
            for k in pos:
                x, y = i + k[0], j + k[1]
                if x>=0 and y>=0 and x<m and y<n and grid[x][y] == 1:
                    fresh -= 1
                    grid[x][y] = 2
                    #print(x,y,minute+1)
                    q.append(((x,y), minute + 1))
            if len(q) == 0:
                t = minute
        return t if not fresh else -1