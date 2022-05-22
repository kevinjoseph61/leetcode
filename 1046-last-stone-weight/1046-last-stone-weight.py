class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(map(lambda x: -x, stones))
        heapq.heapify(heap)
        while(len(heap)>1):
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            z = abs(y-x)
            if z:
                heapq.heappush(heap, -z)
        if not heap:
            return 0
        else:
            return -heap[0]
            