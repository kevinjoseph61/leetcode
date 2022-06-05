class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(tuple(nums[:-1])),self.rob_helper(tuple(nums[1:])))
    
    @functools.cache
    def rob_helper(self, nums):
        #print(nums)
        if nums:
            return max(self.rob_helper(nums[2:])+nums[0], self.rob_helper(nums[1:]))
        else:
            return 0