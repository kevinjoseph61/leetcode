class Solution:
    def processStr(self, s: str) -> str:
        curr = ""
        for i in s:
            if i == '*':
                curr = curr[:-1]
            elif i == '#':
                curr = curr + curr
            elif i == '%':
                curr = curr[::-1]
            else:
                curr += i
        return curr