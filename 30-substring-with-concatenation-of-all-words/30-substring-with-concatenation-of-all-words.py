class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        def search(s, words):
            if all((i==0 for i in words.values())):
                return True
            start = s[:wlen]
            if words[start] > 0:
                words[start] -= 1
                if search(s[wlen:], words):
                    words[start] += 1
                    return True
                words[start] += 1
            return False
        
        wlen = len(words[0])
        ans = []
        cword = Counter(words)
        for i in range(len(s) - len(words)*wlen + 1):
            if search(s[i:], cword):
                ans.append(i)
        
        return ans