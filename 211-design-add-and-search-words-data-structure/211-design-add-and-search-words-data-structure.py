class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.dic[c]
        curr.last = True

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word)
    
    def searchHelper(self, node, word):
        if not word:
            return node.last
        if word[0] == '.':
            for i in node.dic:
                if self.searchHelper(node.dic[i], word[1:]):
                    return True
            return False
        else:
            if word[0] in node.dic:
                return self.searchHelper(node.dic[word[0]], word[1:])
            else:
                return False
        
        
class Trie:
    def __init__(self):
        self.last = False
        self.dic = defaultdict(Trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)