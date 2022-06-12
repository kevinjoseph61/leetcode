class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @functools.cache
        def helper(i, rem):
            if i == len(nums):
                if rem == 0:
                    return 1
                else:
                    return 0
            return helper(i+1, rem-nums[i]) + helper(i+1, rem+nums[i])
        
        return helper(0, target)