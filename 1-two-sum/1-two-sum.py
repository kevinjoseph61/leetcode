class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}
        for i in range(len(nums)):
            pre[nums[i]] = i
        for i in range(len(nums)):
            req = target - nums[i]
            if req in pre and i!=pre[req]:
                return [i, pre[req]]