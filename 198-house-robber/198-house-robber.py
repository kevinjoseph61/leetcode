class Solution:
    
    def rob(self, nums: List[int]) -> int:
        return self.rob_helper(tuple(nums))
    
    @functools.cache
    def rob_helper(self, nums):
        #print(nums)
        if nums:
            return max(self.rob_helper(nums[2:])+nums[0], self.rob_helper(nums[1:]))
        else:
            return 0