class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @functools.cache
        def helper(rem, c):
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            if c >= len(coins):
                return 0
            return helper(rem - coins[c], c) + helper(rem, c+1)
        
        return helper(amount, 0)