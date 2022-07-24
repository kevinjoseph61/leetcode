class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(i, j):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                if i-1 >= 0:
                    return helper(i-1, j)
                else:
                    return False
            if matrix[i][j] < target:
                if j+1 < len(matrix[0]):
                    return helper(i, j+1)
                else:
                    return False
            
        return helper(len(matrix) - 1, 0)
        
        