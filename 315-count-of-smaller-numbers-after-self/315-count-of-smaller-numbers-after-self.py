class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            h = len(enum) // 2
            if h:
                left, right = sort(enum[:h]), sort(enum[h:])
                for i in range(len(enum))[::-1]:
                    if not right or left and right[-1][1] < left[-1][1]:
                        ans[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
                
        enum = list(enumerate(nums))
        ans = [0] * len(nums)
        sort(enum)
        return ans