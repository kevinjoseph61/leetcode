class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @functools.cache
        def pairs(n: int, k: int) -> int:
            max_pairs = (n * (n - 1)) // 2

            if n == 0 or k < 0 or k > max_pairs:  # no inverse pair possible
                return 0
            elif k == 0 or k == max_pairs:  # exactly one inverse pair possible
                return 1
            else:
                return (pairs(n - 1, k) + pairs(n, k - 1) - pairs(n - 1, k - n)) % 1_000_000_007

        return pairs(n, k)
            