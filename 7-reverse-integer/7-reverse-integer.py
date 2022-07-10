class Solution:
    def reverse(self, x: int) -> int:
        s = (x>0) - (x<0)
        n = s*int(str(abs(x))[::-1])
        if n.bit_length() >= 32:
            return 0
        else:
            return n