class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s / 2
        seen = set([0])
        for i in range(len(nums)-1, -1, -1):
            for j in list(seen):
                t = nums[i] + j
                if t == target:
                    return True
                seen.add(t)
        return False