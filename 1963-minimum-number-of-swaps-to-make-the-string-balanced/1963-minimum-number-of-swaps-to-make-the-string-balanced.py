class Solution:
    def minSwaps(self, s: str) -> int:
        curr, m = 0, 0
        for i in s:
            if i == "[":
                curr -= 1
            else:
                curr += 1
                m = max(m, curr)
        return (m + 1) // 2