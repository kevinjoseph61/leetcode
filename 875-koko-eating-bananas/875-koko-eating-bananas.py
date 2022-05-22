class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        m = r
        
        while r >= l:
            mid = (r + l) // 2
            s = 0
            for i in piles:
                s += math.ceil(i/mid)
            
            if s <= h:
                m = min(mid, m)
                r = mid - 1
            else:
                l = mid + 1
                
        return m
        