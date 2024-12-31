#!/usr/bin/env python3

"""
Task Tracker CLI application.
"""

from TaskCLI import TaskTrackerCLI

if __name__ == '__main__':
    TaskTrackerCLI().cmdloop(TaskTrackerCLI.intro)
