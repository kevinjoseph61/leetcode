class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)
        x, y = '0', '0'
        for i in digits:
            if i != '9':
                x = i
                break
        for i in digits:
            if i != '0':
                y = i
                break
        m1 = int(digits.replace(x, '9'))
        m2 = int(digits.replace(y, '0'))
        return m1 - m2