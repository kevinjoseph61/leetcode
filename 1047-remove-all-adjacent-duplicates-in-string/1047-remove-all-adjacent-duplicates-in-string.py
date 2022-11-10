class Solution(object):
    def removeDuplicates(self, S):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)