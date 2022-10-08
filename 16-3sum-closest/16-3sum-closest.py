class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[-3:])
        if res <= target:
            return res
        res = sum(nums[:3])
        if res >= target:
            return res
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                if abs(target - res) > abs(total - target):
                    res = total
                if total > target:
                    k -= 1
                else:
                    j += 1
        return res
                