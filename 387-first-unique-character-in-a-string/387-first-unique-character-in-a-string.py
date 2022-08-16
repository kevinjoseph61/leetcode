class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][1] = d[s[i]][1] + 1
            else:
                d[s[i]] = [i, 1]
        for i in sorted(d.values(), key= lambda x:(x[1], x[0])):
            if i[1] == 1:
                return i[0]
            break
        return -1