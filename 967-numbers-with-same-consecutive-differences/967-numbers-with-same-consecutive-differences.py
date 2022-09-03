class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = deque([1,2,3,4,5,6,7,8,9])
        ans = []
        for j in range(n):
            for i in range(len(nums)):
                #print(nums)
                num = str(nums.popleft())
                if len(num) == n:
                    ans.append(int(num))
                    continue
                ni = int(num[-1])
                p1, p2 = ni+k, ni-k
                if p1 >= 0 and len(str(p1)) == 1:
                    nums.append(int(num + str(p1)))
                if p2 >= 0 and len(str(p2)) == 1 and p1 != p2:
                    nums.append(int(num + str(p2)))
        return ans