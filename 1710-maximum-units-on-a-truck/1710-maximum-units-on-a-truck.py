class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i, t = 0, 0
        while(truckSize):
            if i >= len(boxTypes): break
            z = min(truckSize, boxTypes[i][0])  
            t += z * boxTypes[i][1]
            i += 1
            truckSize -= z
        return t