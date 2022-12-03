class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = []
        for s, count in c.most_common():
            ans.append(s*count)
        return "".join(ans)