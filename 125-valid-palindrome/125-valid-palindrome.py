class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join([y.lower() for y in s if y in string.ascii_letters+string.digits])
        return x == x[::-1]
