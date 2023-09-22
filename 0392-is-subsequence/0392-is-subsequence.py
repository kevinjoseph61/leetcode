class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = 0
        for i in range(len(s)):
            f = False
            for j in range(n, len(t)):
                if s[i] == t[j]:
                    n = j+1
                    f = True
                    break
            if not f:
                break
        else:
            return True
        return False