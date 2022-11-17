class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        max_lx = max(ax1, bx1)
        min_rx = min(ax2, bx2)
        if max_lx<min_rx: #overlap
            x = min_rx-max_lx
        else:
            x = 0
            
        max_ly = max(ay1, by1)
        min_ry = min(ay2, by2)
        if max_ly<min_ry: #overlap
            y = min_ry-max_ly
        else:
            y = 0
            
        return (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1) - x*y