class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cM, cR = Counter(magazine), Counter(ransomNote)        
        for i in set(cR):
            if cR[i] > cM[i]:
                return False
        return True