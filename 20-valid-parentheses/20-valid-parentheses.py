class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i != m[stack.pop()]:
                    return False
        return not bool(stack)
                
                    