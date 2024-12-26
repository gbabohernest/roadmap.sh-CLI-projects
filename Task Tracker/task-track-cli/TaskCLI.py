"""
This module contains the TaskTrackerCLI class, a command-line interface for managing tasks.

Features:
- Add tasks
- View, edit, delete tasks

Usage:
Run the script and interact with the CLI commands.
"""


import os
import json
import cmd
from datetime import datetime


class TaskTrackerCLI(cmd.Cmd):
    """
    Command-line interface for managing tasks.
    Tasks are stored in a JSON file.
    """

    intro = 'Welcome to TaskTracker CLI Application.\nType help or ? to list commands.\n'
    prompt = 'task-cli -> '
    file_path = 'tasks.json'

    def __init__(self):
        super().__init__()
        self.tasks = self.load_tasks()


    def load_tasks(self) -> dict:
        """
        Loads tasks from JSON file if it exits.
        :return: A dictionary of tasks with IDs as keys.
        """

        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8')as fp:
                    return json.load(fp)

            except (FileNotFoundError, json.JSONDecodeError):
                print("Error loading tasks. Starting with an empty task list")

        return {}

