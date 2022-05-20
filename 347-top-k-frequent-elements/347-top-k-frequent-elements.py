import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return list(zip(*freq.most_common()))[0][:k]