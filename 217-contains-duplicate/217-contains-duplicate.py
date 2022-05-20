class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setSoFar = set()
        for i in nums:
            if i in setSoFar:
                return True
            setSoFar.add(i)
        return False