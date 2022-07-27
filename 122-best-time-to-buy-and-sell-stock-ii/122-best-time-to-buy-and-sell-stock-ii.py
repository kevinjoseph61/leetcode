class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        r, l, t = 0, 0, 0
        while(r < len(prices)-1 and l < len(prices)):
            while(r < len(prices)-1 and prices[r] < prices[r+1]):
                r+=1
            #print(l, r,prices[r]-prices[l])
            t += (prices[r]-prices[l])
            l = r = r + 1
        return t