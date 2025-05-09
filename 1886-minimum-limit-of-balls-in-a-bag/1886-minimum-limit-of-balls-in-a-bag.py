class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_balls):
            ops = 0
            for n in nums:
                ops += ceil(n / max_balls) - 1
                if ops > maxOperations:
                    return False
            return True
        
        # O(n * logm)
        l, r = 1, max(nums)
        res = r
        while l < r:
            m = l + ((r - l) // 2)
            if can_divide(m):
                r = m
                res = r
            else:
                l = m + 1
        return res