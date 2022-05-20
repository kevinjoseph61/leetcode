class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        y =  [ [(c,i),(j,c),(c,i//3,j//3)]
                    for i,r in enumerate(board)
                        for j,c in enumerate(r)
                            if c!='.' ] 
        x = []
        for i in y:
            x+=i
        if len(x) == len(set(x)):
            return True
        else:
            return False