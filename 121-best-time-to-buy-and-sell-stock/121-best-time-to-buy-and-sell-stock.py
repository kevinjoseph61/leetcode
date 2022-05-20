class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l, r, m = 0, 1, 0
        while(l<len(prices) and r<len(prices)):
            if prices[l] < prices[r]:
                m = max(m, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return m