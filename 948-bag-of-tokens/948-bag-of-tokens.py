class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i, j, c = 0, len(tokens)-1, 0
        
        while(j >= i):
            if tokens[i] <= power:
                power -= tokens[i]
                c += 1
                i += 1
            elif (j-i) > 1 and c>0:
                power += tokens[j]
                c -= 1
                j -= 1
            else:
                break
        return c
            
            