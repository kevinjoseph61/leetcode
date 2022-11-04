class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vow = []
        for i in range(len(word)):
            if word[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                vow.append(word[i])
                word[i] = "₹"
        vow.reverse()
        j = 0
        for i in range(len(word)):
            if word[i] == "₹":
                word[i] = vow[j]
                j += 1
        return ''.join(word)