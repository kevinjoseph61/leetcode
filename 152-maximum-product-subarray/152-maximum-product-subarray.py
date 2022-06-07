class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        m, n = 1, 1
        for i in nums:
            if i == 0:
                m, n = 1, 1
                continue
            m, n = max(m*i, n*i, i), min(m*i, n*i, i)
            res = max(res, m)
        return res