class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(('a','e','i','o','u','A','E','I','O','U'))
        n1, n2, n = 0 , 0, len(s)
        for i in range(n):
            if s[i] in vowels:
                if i < n//2:
                    n1 += 1
                else:
                    n2 += 1
        return n1 == n2