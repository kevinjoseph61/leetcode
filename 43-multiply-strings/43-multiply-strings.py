class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(i) for i in reversed(num1)]
        num2 = [int(i) for i in reversed(num2)]
        n, m = len(num1), len(num2)
        nums = [0] * (m + n)
        
        for i in range(n):
            for j in range(m):
                s = i + j
                nums[s] += num1[i] * num2[j]
        
        i = 0
        for i in range(len(nums)):
            x = nums[i] // 10
            if x:
                nums[i+1] += x
                nums[i] %= 10
        
        nums.reverse()
        
        for i in range(len(nums)):
            if nums[i]!=0:
                break
        
        return ''.join(list(map(str, nums[i:])))
        