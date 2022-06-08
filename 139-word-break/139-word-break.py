class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #wordDict.sort(key=len, reverse=True)
        @functools.cache
        def helper(s):
            if s == "":
                return True
            for i in wordDict:
                #print(i)
                if s[:len(i)] == i:
                    if helper(s[len(i):]):
                        return True
            return False
        return helper(s)