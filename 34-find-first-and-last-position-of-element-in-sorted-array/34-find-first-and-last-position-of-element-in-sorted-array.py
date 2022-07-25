class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect_right(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]