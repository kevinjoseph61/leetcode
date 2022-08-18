class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        n = len(arr)/2
        total = 0
        ans = 0
        for i in c.most_common():
            total += i[1]
            ans += 1
            if total >= n:
                break
        return ans