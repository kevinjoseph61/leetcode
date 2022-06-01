class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for i in times:
            u, v, w = i
            adj[u].append((w, v))
            
        visit = set()
        heap = [(0, k)]
        m = 0
        
        while heap:
            w, p = heapq.heappop(heap)
            if p in visit:
                continue
            visit.add(p)
            m = max(m, w)
            for i in adj[p]:
                if i[1] in visit:
                    continue
                heapq.heappush(heap, (i[0]+w, i[1]))
                
        return m if len(visit) == n else -1
            