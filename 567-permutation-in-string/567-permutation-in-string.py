class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check1 = [0]*26
        check2 = [0]*26
        i = 0
        for i in range(len(s1)):
            check1[ord(s1[i])-ord('a')] += 1
            if i < len(s2):
                check2[ord(s2[i])-ord('a')] += 1
        if check1 == check2:
            return True
        for i in range(i+1, len(s2)):
            check2[ord(s2[i])-ord('a')] += 1
            check2[ord(s2[i-len(s1)])-ord('a')] -= 1
            if check1 == check2:
                return True
        return False