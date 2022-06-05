class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ""
        l = 0
        for i in range(len(s)):
            k = 0
            while (i-k) >= 0 and (i+k) < len(s) and s[i-k] == s[i+k]:
                k += 1
            k-=1
            t = s[i-k: i+k+1]
            if len(t) > l:
                p, l = t, len(t)
                #print(p, l)
                
            if (i+1) < len(s) and s[i] == s[i+1]:
                k = 0
                while (i-k) >= 0 and (i+1+k) < len(s) and s[i-k] == s[i+1+k]:
                    k += 1
                k-=1
                #print(k,i)
                t = s[i-k: i+k+2]
                if len(t) > l:
                    p, l = t, len(t)
                    #print(p, l)
        return p