class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        status = defaultdict(list)
        count = 0
        for i in words:
            status[i[0]].append(i)
        for i in s:
            t = list(status[i])
            status[i] = []
            for j in t:
                j = j[1:]
                if j:
                    status[j[0]].append(j)
                else:
                    count += 1
        return count
        
            
            