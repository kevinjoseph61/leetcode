class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n, visit = len(board), len(board[0]), set()
        
        def dfs(i, j, visited, flip):
            if i<0 or j<0 or i>=m or j>=n or board[i][j] == "X" or (i, j) in visited:
                return False
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                return True
            visited.add((i, j))
            if flip:
                board[i][j] = "X"
            return bool(dfs(i+1, j, visited, flip) or dfs(i, j+1, visited, flip) or dfs(i-1, j, visited, flip) or dfs(i, j-1, visited, flip))
        
        for i in range(m):
            for j in range(n):
                #print(i, j)
                if board[i][j]=="O" and not dfs(i, j, set(), False):
                    print(i,j)
                    dfs(i, j, set(), True)
        
        
        