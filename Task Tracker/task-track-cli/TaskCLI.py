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
    file_name = 'tasks.json'

    def __init__(self):
        super().__init__()
        self.tasks = self.load_tasks(self.file_name)

    def load_tasks(self, file: str) -> dict:
        """
        Loads tasks from JSON file if it exists.
        :param file: Name of the JSON file.
        :return: A dictionary of tasks with task IDS as keys.
        """

        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as fp:
                    return json.load(fp)
            except json.JSONDecodeError:
                print("Error loading tasks: Corrupted JSON. Starting with an empty task list")

        return {}

    def save_tasks(self, json_file: str, tasks: dict):
        """
        Save tasks to a JSON file.
        :param json_file: File to save our tasks.
        :param tasks: Tasks to be saved.
        """
        try:
            with open(json_file, 'w', encoding='utf-8') as fp:
                json.dump(tasks, fp, indent=4)

        except Exception as e:
            print(f"Error saving tasks: {e}")

    def do_add(self, args: str):
        """
        Command to add a new task.
        Usage: add <description>
        :param args: Task description provided by user.
        """

        description = args.strip()

        if not description:
            print("Error: Task description is required")
            return

        # validate task description to prevent duplication
        if not self.validate_task_description(self.tasks, description): return

        task_id = max(map(int, self.tasks.keys()), default=0) + 1 if self.tasks else 1

        task = {
            'id': task_id,
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),
            'updatedAt': datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        }

        self.tasks[task_id] = task

        try:
            self.save_tasks(self.file_name, self.tasks)
            print(f"Task added successfully (ID: {task_id})")
            return
        except Exception as e:
            print(f"Error in saving task: {e}")

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

    def validate_task_description(self, tasks: dict, des: str) -> bool:
        """
        Validates duplicate task descriptions for better task tracking.
        :param tasks: A dictionary of tasks.
        :param des: Description of task to validate.
        :return: Boolean, True on success, False on failure.
        """

        if tasks and des:
            for task in tasks.values():
                if task['description'].lower() == des.lower():
                    print("Cannot add task, task already exists")
                    return False

        return True
