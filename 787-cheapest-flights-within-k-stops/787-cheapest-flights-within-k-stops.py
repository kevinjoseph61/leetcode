class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0
        t = prices[::]
        
        for i in range(k+1):
            for j in flights:
                s, d, p = j
                if prices[s] == inf:
                    continue
                t[d] = min(prices[s] + p, t[d])
                #print(j, prices, t)
            prices = t[::]
        #print(prices)
        return -1 if prices[dst] == inf else prices[dst]
            