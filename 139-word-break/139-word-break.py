class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                t = len(w)+i
                #print(t, i, w, s[i:t])
                if t<len(s)+1 and s[i:i+len(w)] == w and dp[t]:
                    dp[i] = True
                    break
        #print(dp)
        return dp[0]
            
        