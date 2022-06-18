class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        
        b = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        #print(b)
        n = len(intervals)
        
        if b < n:
            t = newInterval[1]
            s = intervals[b][0]
            while(b < len(intervals) and newInterval[1]>=intervals[b][0]):
                t = intervals[b][1]
                del(intervals[b])
            intervals.insert(b, [min(s, newInterval[0]), max(t, newInterval[1])])
        else:
            intervals.append(newInterval)
            
        return intervals