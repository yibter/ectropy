class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def range(self):
        from datetime import timedelta
        date = self.start
        delta = timedelta(days=1)
        while date <= self.end:
            yield date
            date += delta
    
    def intersection(self, dateRange):
        if self.start is None or self.start < dateRange.start: self.start = dateRange.start
        if self.end is None or self.end > dateRange.end: self.end = dateRange.end
        return self