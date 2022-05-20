class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        l, lmax, r, rmax, water = 0, 0, n-1, 0, 0
        while l < r:
            if height[l]<height[r]:
                water += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
                l += 1
            else:
                water += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
                r -= 1
        return water