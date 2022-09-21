class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        m, n = len(nums1), len(nums2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(n):
            for j in range(m):
                if nums1[j] == nums2[i]:
                    dp[j+1][i+1] = dp[j][i] + 1                    
        
        return max(max(row) for row in dp)