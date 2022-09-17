class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def check(s):
            return True if s==s[::-1] else False
        
        pos = {w: i for i, w in enumerate(words)}
        
        ans = []
        
        for j, w in enumerate(words):
            if check(w) and "" in pos and pos[""] != j:
                ans.append([pos[""], j])
            for i in range(len(w)):
                p, s = w[:i], w[i:]
                if check(s):
                    prev = p[::-1]
                    if prev in pos and pos[prev] != j:
                        ans.append([j, pos[prev]])
                if check(p):
                    srev = s[::-1]
                    if srev in pos and pos[srev] != j:
                        ans.append([pos[srev], j])
        return ans
                