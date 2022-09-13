class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = [bin(i)[2:].zfill(8) for i in data]
        n = len(data)
        i = 0
        while i < n:
            if data[i][0] == "0":
                i += 1
                continue
            if data[i][0:3] == "110":
                if (i+1)<n and data[i+1][0:2] == "10":
                    i += 2
                    continue
                else:
                    return False
            if data[i][0:4] == "1110":
                if (i+2)<n  and data[i+1][0:2] == "10" and data[i+2][0:2] == "10":
                    i += 3
                    continue
                else:
                    return False
            if data[i][0:5] == "11110":
                if (i+3)<n and data[i+1][0:2] == "10" and data[i+2][0:2] == "10" and data[i+3][0:2] == "10":
                    i += 4
                    continue
                else:
                    return False
            return False
        return True