class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, n, l = 0, len(s), 0
        seen = defaultdict(int)
        for r in range(n):
            seen[s[r]] += 1
            i = max(seen.values())
            if ((r - l + 1) - max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res