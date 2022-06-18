class Solution:
    def checkValidString(self, s: str) -> bool:
        maxLeft, minLeft = 0, 0
        for i in s:
            if i == '(':
                minLeft, maxLeft = minLeft + 1, maxLeft + 1
            elif i == ')':
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            else:
                minLeft, maxLeft = minLeft - 1, maxLeft + 1
            if maxLeft < 0:
                return False
            minLeft = max(minLeft, 0)
            
        return True if minLeft <= 0 <= maxLeft else False
                