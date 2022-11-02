class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def diff(x, y):
            d = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    d += 1
            return d
        
        if end not in bank:
            return -1
        if start not in bank:
            bank.append(start)
        
        graph = defaultdict(list)
        
        for i in range(len(bank) - 1):
            for j in range(len(bank)):
                if diff(bank[i], bank[j]) == 1:
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])
        
        visited = set()
        q = deque([start])
        i = 0
        
        while(q):
            for k in range(len(q)):
                w = q.popleft()
                if w == end:
                    return i
                for j in graph[w]:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)
            i += 1
        return -1
                
                
        