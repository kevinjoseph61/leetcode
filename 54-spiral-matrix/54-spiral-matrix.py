class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        t = m * n
        pos = [0, 0]
        visited = set([(0, 0)])
        res = [matrix[0][0]]
        
        while len(visited) < t:
            
            while(pos[1]+1 < n and (pos[0], pos[1]+1) not in visited):
                pos[1] += 1
                res.append(matrix[pos[0]][pos[1]])
                visited.add((pos[0], pos[1]))
                
            while(pos[0]+1 < m and (pos[0]+1, pos[1]) not in visited):
                pos[0] += 1
                res.append(matrix[pos[0]][pos[1]])
                visited.add((pos[0], pos[1]))
            
            while(pos[1]-1 >= 0 and (pos[0], pos[1]-1) not in visited):
                pos[1] -= 1
                res.append(matrix[pos[0]][pos[1]])
                visited.add((pos[0], pos[1]))
                
            while(pos[0]-1 >= 0 and (pos[0]-1, pos[1]) not in visited):
                pos[0] -= 1
                res.append(matrix[pos[0]][pos[1]])
                visited.add((pos[0], pos[1]))
                
        return res
                