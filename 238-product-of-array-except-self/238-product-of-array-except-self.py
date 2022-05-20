class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        p = 1
        n = len(nums)
        for i in range(0,n):
            op.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            op[i] *= p
            p = p * nums[i]
        return op