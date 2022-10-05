class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        key_order = { k: i for i, k in enumerate(" " + order)}
        sorted_words = sorted(words, key=lambda x: [key_order[i] for i in x])
        if sorted_words == words:
            return True
        else:
            return False