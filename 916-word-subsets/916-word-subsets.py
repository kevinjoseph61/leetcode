class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        c = Counter()
        for w in words2:
            c = c | Counter(w)
        return [w for w in words1 if not c - Counter(w)]