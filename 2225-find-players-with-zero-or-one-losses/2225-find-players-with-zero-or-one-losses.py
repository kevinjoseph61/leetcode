class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w, l1, l2 = set(), set(), set()
        for win, lose in matches:
            if win not in w and win not in l1 and win not in l2:
                w.add(win)
            if lose not in l1 and lose not in l2 and lose not in w:
                l1.add(lose)
            elif lose in l1:
                l1.discard(lose)
                l2.add(lose)
            elif lose in w:
                w.discard(lose)
                l1.add(lose)
            #print(w, l1, l2)
        return [sorted(list(w)), sorted(list(l1))]