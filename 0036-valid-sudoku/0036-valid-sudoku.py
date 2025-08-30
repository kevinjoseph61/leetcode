class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = set()
        for r, i in enumerate(board):
            for c, j in enumerate(i):
                if j!='.':
                    for k in [(j, r), (j, c, 'A'), (j, r//3, c//3)]:
                        if k in x:
                            return False
                        x.add(k)
        return True