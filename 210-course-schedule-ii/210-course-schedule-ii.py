class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = { i:[] for i in range(numCourses)} 
        
        order = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()
        done = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in done:
                return True
            if preMap[crs] == []:
                order.append(crs)
                done.add(crs)
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visiting.remove(crs)
            order.append(crs)
            done.add(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return order