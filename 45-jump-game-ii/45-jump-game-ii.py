class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        reached = set()
        q = collections.deque([0])
        while q:
            for _ in range(len(q)):
                j = q.popleft()
                if j == len(nums) - 1:
                    return jumps
                if j >= len(nums) or j in reached:
                    continue
                reached.add(j)
                for k in range(1, nums[j]+1):
                    q.append(j+k)
            jumps += 1
        
        
        