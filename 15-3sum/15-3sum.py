class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1*nums[i]
            j, k = i+1, n-1
            while(j<k):
                total = nums[j]+nums[k]
                if target == total:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while(nums[j]==nums[j-1] and j<k):
                        j += 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return ans