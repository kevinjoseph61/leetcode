class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @functools.cache
        def action(i, buy):
            if i>=len(prices):
                return 0
            
            if buy:
                return max(action(i+1, False) - prices[i], action(i+1, True))
            else:
                return max(action(i+2, True) + prices[i], action(i+1, False))
            
        return action(0, True)