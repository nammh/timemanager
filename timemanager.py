#!python3
"""
Copyright 2018 Moohyeon Nam
Last Modified: 2018. 01. 16

TODO
- Alarm
- Statistics
- Integration with pomodoro
"""
import os
import datetime
import csv
import msvcrt
import timeline

def create_timeline(_title, _tl):
    """
    Finish the idle timeline _tl and
    Create a new timeline and return it
    """
    now = _tl.finish()
    with open("timeline.csv", "a") as ofs:
        writer = csv.writer(ofs)
        writer.writerow((_tl.start, _tl.end, _tl.title))
    time_line = timeline.TimeLine(now)
    time_line.set_title(_title)
    print("Creates a new timeline " + _title + ".")
    return time_line

def finish_timeline(_tl, quit=False):
    """
    Finish the timeline _tl and return idle timeline
    """
    if _tl.title == "Idle" and not quit:
        print("Already Idle.")
        return _tl
    now = _tl.finish()
    with open("timeline.csv", "a") as ofs:
        writer = csv.writer(ofs)
        writer.writerow((_tl.start, _tl.end, _tl.title))
    time_line = timeline.TimeLine(now)
    time_line.set_title("Idle")
    print("Finish the timeline " + _tl.title + ".")
    return time_line

def main_loop(options={}):
    if not os.path.exists("./timeline.csv"):
        with open("timeline.csv", "w") as ofs:
            writer = csv.writer(ofs)
            writer.writerow(("Start", "End", "Task"))
    now = datetime.datetime.now()
    _tl = timeline.TimeLine(now)
    _tl.set_title("Idle")
    while True:
        _input = msvcrt.getch()
        if _input == b"q":
            _tl = finish_timeline(_tl)
            break
        elif _input == b"c":
            _tl = create_timeline(input("> "), _tl)
        elif _input == b"f":
            _tl = finish_timeline(_tl)
        elif _input == b"t":
            now = datetime.datetime.now()
            print(_tl.title + ": " + str(now-_tl.start))
        else:
            print("Command("+str(_input)+") does not exist.")
            print("c: Create timeline.\nf: Finish timeline.\n" +
                  "t: Time spent on the task.\nq: Quit.")

if __name__ == "__main__":
    main_loop()
