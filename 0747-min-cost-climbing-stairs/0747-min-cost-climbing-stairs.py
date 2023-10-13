class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)
        c = cost.copy()
        c.append(0)
        c.append(inf)
        while (i-2) >= 0:
            c[i-1] = min(c[i] + cost[i-1], c[i+1] + cost[i-1])
            c[i-2] = min(c[i-1] + cost[i-2], c[i] + cost[i-2])
            i -= 1
        #print(c)
        return min(c[0], c[1])