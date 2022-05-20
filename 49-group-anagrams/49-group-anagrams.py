import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for i in strs:
            result[str(sorted(i))].append(str(i))
        return [v for k,v in result.items()]