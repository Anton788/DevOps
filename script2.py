#!/usr/bin/env python3
import libtmux
import os
import sys
import csv


server = libtmux.Server()

def start():
    with open("monitoring.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "total", "free", "%usage"])
    session = server.new_session(session_name="homework", kill_session=True)
    wind = session.new_window(attach=False, window_name="start")
    note = f"free -t -s 600 | python3 prepare.py"
    pane = wind.split_window(attach=False)
    pane.send_keys(note)


def stop():
    session = server.find_where({"session_name": "homework"})
    session.kill_session()

def status():
    try:
        session = server.find_where({"session_name": "homework"})
        return "RUNNING"
    except:
        return "STOP"


if __name__ == '__main__':
    arguments = sys.argv
    if arguments[1] == "STOP":
        if status() == "STOP":
            print("ALL PROCESS STOP")
        else:
            stop()
    elif arguments[1] == "START":
        if status() == "RUNNING":
            print("ALREADY RUNNING")
        else:
            start()
    elif arguments[1] == "STATUS":
        print(status())

