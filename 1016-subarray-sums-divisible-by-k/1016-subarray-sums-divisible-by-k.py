class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counts = defaultdict(int)
        counts[0] = 1
        pre = 0
        ans = 0
        for i in nums:
            pre += i
            m = pre % k
            ans += counts[m]
            counts[m] += 1
            
        return ans