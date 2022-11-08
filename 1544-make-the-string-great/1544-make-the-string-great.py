class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        
        while True:
            b = False
            i = 0
            while i < len(s) - 1:
                if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    del(s[i])
                    del(s[i])
                    b = True
                else:
                    i += 1
                #print(s)
            if not b:
                break
        
        return "".join(s)