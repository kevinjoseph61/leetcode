class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        p = math.log(n, 4)
        if p == int(p):
            return True
        else:
            return False