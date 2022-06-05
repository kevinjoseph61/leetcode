class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 0
        for i in range(len(s)):
            k = 0
            while (i-k) >= 0 and (i+k) < len(s) and s[i-k] == s[i+k]:
                k += 1
            n+=k
            k-=1
                
            if (i+1) < len(s) and s[i] == s[i+1]:
                k = 0
                while (i-k) >= 0 and (i+1+k) < len(s) and s[i-k] == s[i+1+k]:
                    k += 1
                n += k
                
        return n