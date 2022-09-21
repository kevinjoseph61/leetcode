class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ans = []
        s = sum([i for i in nums if i%2==0])
        
        for n, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
            nums[i] += n
            if nums[i] % 2 == 0:
                s += nums[i]
            ans.append(s)
        
        return ans