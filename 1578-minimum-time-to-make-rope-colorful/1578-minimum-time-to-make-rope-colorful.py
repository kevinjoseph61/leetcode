class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, ans = 0, 0
        while i < len(colors):
            j = i
            while j<len(colors)-1 and colors[j] == colors[j+1]:
                j += 1
            if i!=j:    
                l = neededTime[i:j+1]
                ans += sum(l) - max(l)
                i = j - 1
            i += 1
        return ans