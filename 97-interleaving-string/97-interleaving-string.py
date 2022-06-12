class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @functools.cache
        def helper(s1, s2, s3):
            if s1 and s2:
                if len(s1)+len(s2) != len(s3):
                    return False
                b = False
                if s1[0] == s3[0]:
                    b = b or helper(s1[1:], s2, s3[1:])
                if s2[0] == s3[0]:
                    b = b or helper(s1, s2[1:], s3[1:])
                return b
            else:
                return s1+s2 == s3
            
        return helper(s1, s2, s3)