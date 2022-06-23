class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits[0] += 1
        carry = 0
        for i in range(len(digits)):
            if carry == 1:
                digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits