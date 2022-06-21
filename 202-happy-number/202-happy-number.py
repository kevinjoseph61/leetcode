class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            n = sum([int(k)**2 for k in str(n)])
            if n == 1:
                return True
        return False
                