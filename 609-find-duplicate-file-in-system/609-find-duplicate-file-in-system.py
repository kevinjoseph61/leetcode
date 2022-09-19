class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        r = re.compile(r'(.+)\((.+)\)')
        
        for p in paths:
            s = p.split(' ')
            for i in s[1:]:
                m = r.search(i)
                if m:
                    ans[m.group(2)].append(s[0] + '/' + m.group(1))
        
        return [ans[k] for k in ans if len(ans[k])>1]