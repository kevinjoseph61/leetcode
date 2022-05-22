class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        q = collections.deque()
        time = 0
        
        while maxHeap or q:
            
            
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
            time += 1
        
        return time
            