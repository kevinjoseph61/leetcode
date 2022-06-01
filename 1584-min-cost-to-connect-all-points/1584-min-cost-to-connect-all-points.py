class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
                
        heap = [(0, 0)]
        visit = set()
        total = 0
        
        while len(visit) != n:
            dist, p = heapq.heappop(heap)
            while p in visit:
                dist, p = heapq.heappop(heap)
            visit.add(p)
            total += dist
            for i in adj[p]:
                if i[1] not in visit:
                    heapq.heappush(heap, i)
        
        return total
            
            
                    