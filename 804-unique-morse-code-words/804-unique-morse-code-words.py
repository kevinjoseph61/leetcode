class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uni = set()
        alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            s = ""
            for i in w:
                s += alpha[ord(i)-97]
            uni.add(s)
        return len(uni)