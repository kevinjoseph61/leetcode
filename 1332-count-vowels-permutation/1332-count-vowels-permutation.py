class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [([1] + [0 for i in range(n-1)]) for j in range(5)]
        
        for i in range(1, n):
            dp[0][i] = dp[1][i-1] + dp[2][i-1] + dp[4][i-1]
            dp[1][i] = dp[0][i-1] + dp[2][i-1]
            dp[2][i] = dp[1][i-1] + dp[3][i-1]
            dp[3][i] = dp[2][i-1]
            dp[4][i] = dp[2][i-1] + dp[3][i-1]
        
        return (dp[0][n-1] + dp[1][n-1] + dp[2][n-1] + dp[3][n-1] + dp[4][n-1]) % 1_000_000_007