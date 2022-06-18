class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize:
            return False
        
        c = Counter(hand)
        for i in sorted(c):
            while(c[i] > 0):
                c[i] -= 1
                for j in range(1, groupSize):
                    if (i+j) not in c or c[i+j] <= 0:
                        return False
                    c[i+j] -= 1
                
        return True