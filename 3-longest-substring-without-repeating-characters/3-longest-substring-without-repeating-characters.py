class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, m, n = 0, 1, 1, len(s)
        if n <= 1:
            return n
        check = set()
        for r in range(0, n):
            if s[r] in check:
                while s[r] in check:
                    check.remove(s[l])
                    l += 1
            check.add(s[r])
            m = max(m, r - l + 1)
        return m
            