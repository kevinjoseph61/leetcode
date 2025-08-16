class Solution:
    def maximum69Number (self, num: int) -> int:
        numslist = list(str(num))
        for i in range(len(numslist)):
            if numslist[i] == '6':
                numslist[i] = '9'
                break
        return int("".join(numslist))