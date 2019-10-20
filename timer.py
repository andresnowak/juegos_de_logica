#!/usr/bin/env python
'''
|| Name: Andres Nowak
|| Date: Thu Oct 17 15:04:27 CDT 2019
'''
from threading import Thread
from time import sleep, ctime, time

class Time(Thread):
    def __init__(self, threadId, name, count):
        Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("starting: " + self.name + "\n")
        print_time(self.name, 1, self.count)
        print("exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        sleep(delay)
        print(f"count: {count}")
        count -= 1