class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        tickets.sort()
        ticks = defaultdict(list)
        order = ["JFK"]
        for i in tickets:
            ticks[i[0]].append(i[1])
        
        def dfs(place, n):
            #print(place, n, ticks, order)
            if n == 0:
                raise KeyError
            for i in range(len(ticks[place])):
                dest = ticks[place].pop(i)
                order.append(dest)
                dfs(dest, n-1)
                order.pop()
                ticks[place].insert(i, dest)
        
        #dfs("JFK", n)
        try:
            dfs("JFK", n)
        except Exception as e:
            return order
        return []
                
                