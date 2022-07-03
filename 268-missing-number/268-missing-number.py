class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        req = n*(n+1) // 2
        return req - s