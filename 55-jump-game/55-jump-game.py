class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @functools.cache
        def helper(i):
            if i >= n - 1:
                return True
            for j in range(nums[i], 0, -1):
                if helper(i+j):
                    return True
            return False
        
        return helper(0)