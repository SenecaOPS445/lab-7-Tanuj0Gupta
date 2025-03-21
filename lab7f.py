#!/usr/bin/env python3
# Student ID: 162349229

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Methods: __init__, __str__, __repr__, __add__,
                format_time, time_to_sec, sum_times,
                change_time, valid_time
    """
    
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Used by print() to display formatted time"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Used in the Python shell to represent the object"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload + operator to add two Time objects"""
        return self.sum_times(t2)

    def format_time(self):
        """Return a formatted time string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def time_to_sec(self):
        """Convert time to total seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def sum_times(self, t2):
        """Add another Time object and return a new Time object"""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Add or subtract seconds from this Time object"""
        total_seconds = self.time_to_sec() + seconds
        nt = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def valid_time(self):
        """Check if the time values are valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True


# Utility function remains outside the class
def sec_to_time(seconds):
    """Convert seconds to a Time object (hh:mm:ss)"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
