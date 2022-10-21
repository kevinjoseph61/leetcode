class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s, j = set(), 0
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if i >= k:
                s.remove(nums[j])
                j += 1
        return False
            