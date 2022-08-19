class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        end = defaultdict(int)
        for i in nums:
            if not c[i]:
                continue
            if end[i] > 0:
                c[i] -= 1
                end[i] -= 1
                end[i+1] += 1
                continue
            if c[i+1] and c[i+2]:
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                end[i+3] += 1
                continue
            return False
        return True
                