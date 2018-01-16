#!python3
"""
Copyright 2018 Moohyeon Nam
Last Modified: 2018. 01. 16
"""
import datetime

class TimeLine:
    """
    This is a TimeLine class.
    """
    def __init__(self, _start):
        self.start = _start
        self.end = None
        self.title = ""

    def __repr__(self):
        if self.end != None:
            return self.title + ": " + self.start.strftime("%H:%M:%S")\
                + " ~ " + self.end.strftime("%H:%M:%S")
        else:
            return self.title + ": " + self.start.strftime("%H:%M:%S") + " ~ "

    def __cmp__(self, other):
        if self.start < other.start:
            return -1
        elif self.start == other.start:
            return 0
        else:
            return 1

    def __add__(self, other):
        if self < other:
            self.end = other.end
            return self
        else:
            other.end = self.end
            return other

    def reset(self):
        """
        Reset the starting time.
        """
        self.start = datetime.datetime.now()

    def finish(self):
        """
        End the timer.
        """
        self.end = datetime.datetime.now()
        return self.end

    def set_title(self, _title):
        """
        Set the title of this timeline.
        """
        self.title = _title


if __name__ == "__main__":
    t = TimeLine()
    print(t)
    t.set_title("New")
    print(t)
    t.finish()
    print(t)
