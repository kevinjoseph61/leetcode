class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
         