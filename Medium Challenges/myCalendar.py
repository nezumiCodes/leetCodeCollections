'''
- Create a calendar
- Don't permit double booking (same time, same day, or intersecting time)
- We represent event as a pair of integers [start, end), start <= x < end
  (strict start, flexible end --> can end before the actual declared end time)
'''

class MyCalendar:
    def __init__(self):
        self.calendar = [] 
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s<end and start<e:
                return False
        self.calendar.append((start,end))
        return True