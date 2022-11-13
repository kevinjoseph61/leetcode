class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides = sorted(rides)
        S = [i[0] for i in rides]
        
        m = len(rides)
        dp = [0]*(m+1)
        for k in range(m-1, -1, -1):
            temp = bisect_left(S, rides[k][1])
            dp[k] = max(dp[k+1], rides[k][2] - rides[k][0] + rides[k][1] + dp[temp])
            
        return dp[0]