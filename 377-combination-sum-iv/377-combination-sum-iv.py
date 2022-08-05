class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    dp[i] += 1
                if num < i:
                    dp[i] += dp[i-num]
        
        return dp[target]
            