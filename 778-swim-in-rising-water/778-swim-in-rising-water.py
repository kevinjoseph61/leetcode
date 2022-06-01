class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], (0, 0))]
        visit = set()
        while heap:
            w, pos = heapq.heappop(heap)
            #print(w, pos)
            if pos == (n-1, n-1):
                return w
            if pos in visit:
                continue
            visit.add(pos)
            i, j = pos
            x, y = i+1, j
            if x<n and y<n and x>=0 and y>=0 and (x, y) not in visit:
                heapq.heappush(heap, (max(grid[x][y], w), (x, y)))
            x, y = i, j + 1
            if x<n and y<n and x>=0 and y>=0 and (x, y) not in visit:
                heapq.heappush(heap, (max(grid[x][y], w), (x, y)))
            x, y = i-1, j
            if x<n and y<n and x>=0 and y>=0 and (x, y) not in visit:
                heapq.heappush(heap, (max(grid[x][y], w), (x, y)))
            x, y = i, j - 1
            if x<n and y<n and x>=0 and y>=0 and (x, y) not in visit:
                heapq.heappush(heap, (max(grid[x][y], w), (x, y)))

            