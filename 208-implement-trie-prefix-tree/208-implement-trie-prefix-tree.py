class Trie:

    def __init__(self):
        self.root = TrieObj()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            curr = curr.dic[c]
        curr.last = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.dic:
                return False
            curr = curr.dic[c]
        return curr.last
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.dic:
                return False
            curr = curr.dic[c]
        return True
        
class TrieObj:
    def __init__(self):
        self.last = False
        self.dic = defaultdict(TrieObj)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)