class Solution:
    def maximumScore(self, nums: List[int], multi: List[int]) -> int:
        
        def solve(l, r, i):
            #print(l,r,i)
            if i >= len(multi):
                return 0
            if dp[l][i] != -1001:
                return dp[l][i]
            
            dp[l][i] = max(multi[i] * nums[l] + solve(l+1, r, i+1), multi[i] * nums[r] + solve(l, r-1, i+1))
            return dp[l][i]
            
        dp = [[-1001 for _ in range(1001)] for _ in range(1001)]
        return solve(0, len(nums)-1, 0)
        