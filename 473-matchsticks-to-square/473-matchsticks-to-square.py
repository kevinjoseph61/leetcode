class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = [0] * 4
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        
        def check(i):
            if i == len(matchsticks):
                return 1 == len(set(s))
            
            for j in range(4):
                s[j] += matchsticks[i]
                if s[j] <= target and check(i+1):
                    return True
                s[j] -= matchsticks[i]
                
                if s[j] == 0:
                    break
                
            return False
                
        return check(0)