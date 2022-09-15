class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        ans = []
        for i in sorted(c):
            if i == 0:
                if c[i]%2 == 0:
                    ans.extend([i for _ in range(c[i]//2)])
                    continue
                else:
                    return []
            if c[i]:
                if c[i] <= c[2*i]:
                    ans.extend([i for _ in range(c[i])])
                    c[2*i] -= c[i]
                    c[i] = 0
                else:
                    return []
        return ans