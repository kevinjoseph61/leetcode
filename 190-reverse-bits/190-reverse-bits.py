class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        b = ('0' * (32 - len(b))) + b
        b = b[::-1]
        return int(b, 2)
        