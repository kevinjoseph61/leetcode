class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @functools.cache
        def helper(s, p):
            #print("s:",s,"p:", p)
            if p:
                if len(p) >= 2:
                    if p[1] == "*":
                        if p[0] == ".":
                            for i in range(len(s)+1):
                                if helper(s[i:], p[2:]):
                                    return True
                            return False
                        if helper(s, p[2:]):
                            return True
                        i = 0
                        while i < len(s) and p[0] == s[i]:
                            if helper(s[i+1:], p[2:]):
                                return True
                            i += 1
                        return False
                if s and (p[0] == "." or s[0] == p[0]):
                    return helper(s[1:], p[1:])
                return False
            return False if s or p else True
        
        return helper(s, p)
                
                        