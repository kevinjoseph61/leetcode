class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.found = False
        try:
            for i in range(self.m):
                for j in range(self.n):
                    self.backtrack((i,j), set(), word)
        except Exception as e:
            pass
        return self.found

                
    def backtrack(self, pos, visited, word):
        i, j = pos
        if i < 0 or j < 0 or i >= self.m or j >= self.n or pos in visited or word[0] != self.board[i][j]:
            return
        visited.add(pos)
        if len(word) == 1:
            self.found = True
            raise KeyError
        self.backtrack((i+1,j), visited, word[1:])
        self.backtrack((i,j+1), visited, word[1:])
        self.backtrack((i-1,j), visited, word[1:])
        self.backtrack((i,j-1), visited, word[1:])
        visited.discard(pos)