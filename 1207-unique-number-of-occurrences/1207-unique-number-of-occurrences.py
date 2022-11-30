class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        counts = set()
        for k, v in c.items():
            if v in counts:
                return False
            else:
                counts.add(v)
        return True
            