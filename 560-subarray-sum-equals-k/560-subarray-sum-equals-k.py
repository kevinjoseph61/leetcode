class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre, s, ans = defaultdict(int), 0, 0
        pre[0] = 1
        for i in nums:
            s += i
            if s-k in pre:
                ans = ans + pre[s-k]
            pre[s] = pre[s] + 1
        return ans