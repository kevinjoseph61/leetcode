class Solution:
    def minExtraChar(self, start: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(s):
            #print(s)
            if not s:
                return 0
            m = inf
            for i in dictionary:
                if s.startswith(i):
                    m = min(m, dp(s[len(i):]))
            m = min(1 + dp(s[1:]), m)
            return m
        
        return dp(start)