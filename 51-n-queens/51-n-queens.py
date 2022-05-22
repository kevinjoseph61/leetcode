class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n for i in range(n)]
        res = []
        def safe(i, j):
            x, y = i-1, j-1
            while(x>=0 and y>=0):
                if board[x][y] == "Q":
                    return False
                x, y = x-1, y-1
            x, y = i+1, j+1
            while(x<n and y<n):
                if board[x][y] == "Q":
                    return False
                x, y = x+1, y+1
            x, y = i-1, j+1
            while(x>=0 and y<n):
                if board[x][y] == "Q":
                    return False
                x, y = x-1, y+1
            x, y = i+1, j-1
            while(x<n and y>=0):
                if board[x][y] == "Q":
                    return False
                x, y = x+1, y-1
            x, y = 0, j
            while(x<n):
                if board[x][y] == "Q":
                    return False
                x += 1
            x, y = i, 0
            while(y<n):
                if board[x][y] == "Q":
                    return False
                y += 1
            return True
        
        def check(i):
            for j in range(n):
                if safe(i, j):
                    #print(board)
                    board[i] = board[i][:j] + "Q" + board[i][j+1:]
                    if i == n-1:
                        res.append(board.copy())
                        board[i] = "."*n
                        return
                    check(i+1)
                    board[i] = "."*n
        
        check(0)
        return res
        
        
                    
            
            