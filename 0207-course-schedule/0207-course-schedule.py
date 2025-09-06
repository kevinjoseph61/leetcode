class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in prerequisites:
            adj[i[0]].append(i[1])
        complete = set()
        visited = set()
        
        def dfs(i):
            
            if i in complete:
                return True
            if i in visited:
                return False
            visited.add(i)
            for j in reversed(adj[i]):
                if dfs(j):
                    adj[i].remove(j)
                else:
                    raise KeyError
            if len(adj[i]) == 0:
                complete.add(i)
                visited.remove(i)
                return True
            else:
                raise KeyError
        
        for i in list(adj):
            try:
                if not dfs(i):
                    return False
            except:
                return False
        return True