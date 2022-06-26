class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1, len(dp)):
            dp[i] = 1 + dp[i&(i-1)]
            
        return dp