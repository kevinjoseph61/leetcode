class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        i = 0
        
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i+1][0]:
                if intervals[i][1] > intervals[i+1][1]:
                    del(intervals[i])  
                else:
                    del(intervals[i+1])
            else:
                i += 1
        
        return n - len(intervals)