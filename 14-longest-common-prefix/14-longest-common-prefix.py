class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        s = list(zip(*strs))
        for i in s:
            if len(set(i)) == 1:
                pre += i[0]
            else:
                break
        return pre