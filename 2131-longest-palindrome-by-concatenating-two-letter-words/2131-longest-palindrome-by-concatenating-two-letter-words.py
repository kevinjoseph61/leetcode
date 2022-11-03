class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        mid = 0
        length = 0
        for w in c:
            if w == w[::-1]:
                if c[w] % 2 == 0:
                    length += c[w] * 2
                else:
                    if c[w] > 1:
                        length += (c[w]-1) * 2
                    if mid == 0:
                        mid = 2
            elif c[w]> 0 and w[::-1] in c and c[w[::-1]] > 0:
                length += min(c[w], c[w[::-1]]) * 4
                c[w], c[w[::-1]] = 0, 0
        return length + mid
                        