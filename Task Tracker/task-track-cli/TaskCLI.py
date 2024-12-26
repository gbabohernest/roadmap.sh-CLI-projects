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
        Loads tasks from JSON file if it exists.
        :return: A dictionary of tasks with IDs as keys.
        """

        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as fp:
                    return json.load(fp)

            except (FileNotFoundError, json.JSONDecodeError):
                print("Error loading tasks. Starting with an empty task list")

        return {}

    def save_tasks(self):
        """
        Save tasks to a JSON file.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as fp:
                json.dump(self.tasks, fp, index=4)

        except Exception as e:
            print(f"Error saving tasks: {e}")

    def do_exit(self, arg) -> bool:
        """
        Command to exits the application.
        Usage: exit
        """
        print('Goodbye.Thanks for checking out the Application.')
        return True

    def do_EOF(self, arg) -> bool:
        """
        Command to exits the application when EOF signal is received.
        Usage: EOF (Ctrl+D)
        """
        print("")
        return True
