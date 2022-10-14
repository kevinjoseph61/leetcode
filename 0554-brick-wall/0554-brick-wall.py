class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        for row in wall:
            s = 0
            for i in row:
                s += i
                count[s] += 1
        del count[sum(wall[0])]
        return len(wall) - (max(count.values()) if count.values() else 0)