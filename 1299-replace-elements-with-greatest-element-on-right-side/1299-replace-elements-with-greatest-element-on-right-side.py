class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            t = arr[i]
            arr[i] = m
            m = max(m, t)
        return arr