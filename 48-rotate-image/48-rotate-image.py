class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        t, b, l, r = 0, n-1, 0, n-1
        
        while (t<=b and l<=r):
            
            for i in range(r - l):
                matrix[t][l+i], matrix[t+i][r], matrix[b][r-i], matrix[b-i][l] = matrix[b-i][l], matrix[t][l+i], matrix[t+i][r], matrix[b][r-i]
                
            t+=1
            b-=1
            l+=1
            r-=1
        