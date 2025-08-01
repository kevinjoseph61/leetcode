class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        for i in range(1, numRows):
            t = [1]
            for j in range(len(tri[i-1])-1):
                t.append(tri[i-1][j] + tri[i-1][j+1])
            t.append(1)
            tri.append(t)
        return tri