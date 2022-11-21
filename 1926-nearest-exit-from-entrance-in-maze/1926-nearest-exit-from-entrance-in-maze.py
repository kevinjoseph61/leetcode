class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = 'x'
        q = deque([entrance])
        steps = 1
        while(q):
            for _ in range(len(q)):
                pos = q.popleft()
                for add in [[0,1], [1,0], [-1,0], [0,-1]]:
                    new = [pos[0]+add[0], pos[1]+add[1]]
                    if 0 <= new[0] < m and 0 <= new[1] < n and maze[new[0]][new[1]] == '.': 
                        if (new[0] == 0 or new[0] == m-1 or new[1] == 0 or new[1] == n-1):
                            return steps
                        else:
                            maze[new[0]][new[1]] = 'x'
                            q.append(new)
            steps += 1
        return -1