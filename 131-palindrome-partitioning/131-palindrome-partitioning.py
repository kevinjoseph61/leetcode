class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(pos, st, curr):
            if st=="":
                res.append(curr[::])
                return
            for i in range(pos+1, len(s)+1):
                st = s[pos:i]
                if st == st[::-1]:
                    curr.append(st)
                    dfs(i, s[i:], curr)
                    curr.pop()
        dfs(0, s, [])
        return res