class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i in range(len(digits)):
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] %= 10
            else:
                break
        else:
            digits.append(1)
        digits.reverse()
        return digits