class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique = set(sentence)
        for s in string.ascii_lowercase:
            if s not in unique:
                return False
        return True