class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        N = len(arr)
        prefix_cnt = [0] * 1001 # prefix counts
        # prefix_cnt[x] -> count of nums <= x
        # upper

        for j in range(N - 1):
            for k in range(j + 1, N):
                if abs(arr[j] - arr[k]) <= b:
                    # how many values before j
                    # where abs conditions are met
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)
                    
                    l = max(l, 0)
                    r = min(r, 1000)

                    if l <= r:
                        res += prefix_cnt[r] - (0 if l == 0 else prefix_cnt[l-1])

            for index in range(arr[j], 1001):
                prefix_cnt[index] += 1
        return res