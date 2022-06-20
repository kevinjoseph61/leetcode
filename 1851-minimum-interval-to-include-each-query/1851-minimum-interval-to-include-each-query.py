class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        heap = []
        res = {}
        n = len(intervals)
        q = sorted(set(queries))
        intervals.sort()
        
        i = 0
        for j in q:
            while(i < n and intervals[i][1] < j):
                i += 1
            while(i < n and intervals[i][0] <= j ):
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while(heap and heap[0][1] < j):
                heapq.heappop(heap)
            if heap:
                res[j] = heap[0][0]
            else:
                res[j] = -1
        
        return [res[k] for k in queries]
        