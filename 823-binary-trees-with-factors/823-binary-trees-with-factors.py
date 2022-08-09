class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = set(arr)
        
        @functools.cache
        def dp(n):
            ret = 1
            for c in s:
                if n%c == 0 and n//c in s:
                    ret += dp(c) * dp(n//c)
            return ret
            
        ans = 0
        for i in s:
            ans += dp(i)
        return ans % 1_000_000_007