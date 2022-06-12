class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @functools.cache
        def helper(s, t):
            if s and t:
                if s[0] == t[0]:
                    return helper(s[1:], t[1:])
                else:
                    return 1 + min(helper(s[1:], t[1:]), helper(s[1:], t), helper(s, t[1:]))
            else:
                return len(s or t)
            
        return helper(word1, word2)