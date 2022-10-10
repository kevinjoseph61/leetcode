class Solution:
    def numSquares(self, n: int) -> int:
        arr, i = [], 1
        while i**2 <= n:
            arr.append(i**2)
            i += 1
        
        #one-sum O(N^(1/2))
        if n in arr:
            return 1
        
        #two-sum O(N)
        for e in arr:
            if n-e in arr:
                return 2
        
        #three-sum O(N)
        arr_set = set(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if n-arr[i]-arr[j] in arr_set:
                    return 3
        
        #four-sum O(1)
        return 4