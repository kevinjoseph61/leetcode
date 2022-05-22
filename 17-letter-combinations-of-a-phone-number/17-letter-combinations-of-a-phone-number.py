class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def dfs(s, curr):
            if not s:
                if curr:
                    res.append("".join(curr))
                return
            for i in map[s[0]]:
                curr.append(i)
                dfs(s[1:], curr)
                curr.pop()
        dfs(digits, [])
        return res