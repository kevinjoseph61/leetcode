class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.board = heights
        self.m, self.n = len(heights), len(heights[0])
        res = []
        for i in range(self.m):
            for j in range(self.n):
                if self.pacific(i, j, set(), inf) and self.atlantic(i, j, set(), inf):
                    res.append([i,j])
        return res
        
    def pacific(self, i, j, visited, prev):
        if i<0 or j<0 or i>=self.m or j>=self.n or self.board[i][j] > prev or (i, j) in visited:
            return False
        if i == 0 or j == 0:
            return True
        visited.add((i, j))
        ret = bool(self.pacific(i+1, j, visited, self.board[i][j]) or self.pacific(i, j+1, visited, self.board[i][j]) or self.pacific(i-1, j, visited, self.board[i][j]) or self.pacific(i, j-1, visited, self.board[i][j]))
        visited.discard((i, j))
        return ret
    
    def atlantic(self, i, j, visited, prev):
        if i<0 or j<0 or i>=self.m or j>=self.n or self.board[i][j] > prev or (i, j) in visited:
            return False
        if i == self.m-1 or j == self.n-1:
            return True
        visited.add((i, j))
        ret = bool(self.atlantic(i+1, j, visited, self.board[i][j]) or self.atlantic(i, j+1, visited, self.board[i][j]) or self.atlantic(i-1, j, visited, self.board[i][j]) or self.atlantic(i, j-1, visited, self.board[i][j]))
        visited.discard((i, j))
        return ret