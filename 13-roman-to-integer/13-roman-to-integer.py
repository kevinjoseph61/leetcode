class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        
        total, i = 0, 0
        while i < len(s):
            if i < (len(s)-1):
                if value[s[i]] < value[s[i+1]]:
                    total += value[s[i+1]] - value[s[i]]
                    i += 1
                else:
                    total += value[s[i]]
            else:
                total += value[s[i]]
            i += 1
        
        return total