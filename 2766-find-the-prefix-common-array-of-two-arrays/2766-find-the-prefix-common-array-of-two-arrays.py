class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b = set(), set()
        ans, count = [], 0
        for i, j in zip(A, B):
            a.add(i)
            b.add(j)
            if i in b:
                count += 1
            if j in a:
                count += 1
            if i == j:
                count -= 1
            ans.append(count)
        return ans