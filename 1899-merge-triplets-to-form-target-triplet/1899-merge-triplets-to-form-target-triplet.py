class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        def check(c):
            if c[0] > target[0] or c[1] > target[1] or c[2] > target[2]:
                return False
            return True
        
        triplets = list(filter(check, triplets))
        
        if not triplets:
            return False
        
        t = list(zip(*triplets))
        #print(triplets, t)
        
        return True if target[0] in t[0] and target[1] in t[1] and target[2] in t[2] else False
            