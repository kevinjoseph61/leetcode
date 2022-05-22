class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dic[key]) == 0:
            return ""
        pos = bisect.bisect_right(self.dic[key], timestamp, key=lambda x:x[1])
        pos = pos - 1
        if pos < 0 or self.dic[key][pos][1] > timestamp :
            return ""
        return self.dic[key][pos][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)