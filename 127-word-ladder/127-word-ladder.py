class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        nei = defaultdict(list)
        wordList.append(beginWord)
        for i in wordList:
            for j in range(n):
                nei[i[:j] + "*" + i[j+1:]].append(i)
        visit = set([beginWord]) 
        q = deque([beginWord])
        level = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for w in nei[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)
            level += 1
        return 0