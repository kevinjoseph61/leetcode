class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @functools.cache
        def helper(s, t):
            if not t:
                return 1
            if not s:
                return 0
            total = 0
            if s[0] == t[0]:
                total += helper(s[1:], t[1:])
            total += helper(s[1:], t)
            
            return total
        
        return helper(s, t)