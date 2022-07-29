class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        @functools.cache
        def normalize(word):
            d = {}
            s = string.ascii_lowercase
            i = 0
            for w in word:
                if w not in d:
                    d[w] = s[i]
                    i += 1
            return ''.join([d[i] for i in word])
        
        p = normalize(pattern)
        ans = []
        for w in words:
            if p == normalize(w):
                ans.append(w)
        return ans