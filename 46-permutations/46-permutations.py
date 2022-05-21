class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(curr, num):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in num:
                curr.append(i)
                check = num.copy()
                check.remove(i)
                helper(curr, check)
                curr.pop()
                
        helper([], set(nums))
        return res
                