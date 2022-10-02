class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @functools.cache
        def recurse(s, n):
            if n == 0:
                return 1 if s == 0 else 0
            ret = 0
            for i in range(1, k+1):
                ret += recurse(s-i, n-1)
            return ret
        
        return recurse(target, n) % 1_000_000_007
        