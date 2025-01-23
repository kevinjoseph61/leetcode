class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        # Rows
        for r in range(ROWS):
            row_sum = sum(grid[r])
            if row_sum <= 1:
                # Don't mark
                continue
            res += row_sum
            
            for c in range(COLS):
                if grid[r][c]:
                    grid[r][c] = -1 # Mark

        # Cols            
        for c in range(COLS):
            col_sum = 0
            unmarked = 0
            for r in range(ROWS):
                col_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1 # Unmark
            if col_sum >= 2:
                res += unmarked
        
        return res