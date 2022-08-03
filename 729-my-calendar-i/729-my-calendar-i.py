class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect(self.bookings, start, key=lambda x: x[0])
        #print(self.bookings, i)
        if 0 <= i-1 < len(self.bookings) and self.bookings[i-1][1] > start:
            return False
        if i < len(self.bookings) and self.bookings[i][0] < end:
            return False
        self.bookings.insert(i, [start, end])
        return True
    
    

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)