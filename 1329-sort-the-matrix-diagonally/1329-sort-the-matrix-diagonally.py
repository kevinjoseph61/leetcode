class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m-1, -1, -1):
            arr = [mat[x][x-i] for x in range(i, m) if (x-i)<n]
            arr.sort()
            for x in range(i, m):
                if x-i < n:
                    mat[x][x-i] = arr[x-i]
        for i in range(n-1, -1, -1):
            arr = [mat[x-i][x] for x in range(i, n) if (x-i)<m]
            arr.sort()
            for x in range(i, n):
                if x-i < m:
                    mat[x-i][x] = arr[x-i]
        return mat
            