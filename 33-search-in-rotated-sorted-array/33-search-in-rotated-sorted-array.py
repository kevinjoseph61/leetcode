class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while(r>=l):
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            elif nums[l]<=nums[mid] and target<nums[l]:
                l = mid + 1
            elif nums[l]<=nums[mid] and target>nums[mid]:
                l = mid + 1
            elif nums[l]<=nums[mid]:
                r = mid - 1 
            elif nums[r]>=nums[mid] and target>nums[r]:
                r = mid - 1 
            elif nums[r]>=nums[mid] and target<nums[mid]:
                r = mid - 1 
            else:
                l = mid + 1
        return -1