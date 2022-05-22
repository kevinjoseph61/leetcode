class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def recurse(opened, closed):
            if opened == closed == n:
                res.append(''.join(stack))
                return
            
            if opened < n:
                stack.append('(')
                recurse(opened+1, closed)
                stack.pop()
            
            if closed < n and closed < opened:
                stack.append(')')
                recurse(opened, closed+1)
                stack.pop()
        
        recurse(0, 0)
            
        return res