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
from xmlrpc.client import DateTime


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

    def do_delete(self, arg: str):
        """
        Command to delete a task.
        Usage: delete <task_ID>
        :param arg: ID of the task to delete.
        """

        task_id = arg.strip()

        if not task_id:
            print("Error: Please provide the ID of the task.\nUsage: delete <task_ID>.")
            return

        # load tasks
        if not self.tasks:
            print("Error: No tasks available to delete. Add tasks.")
            return

        if task_id not in self.tasks:
            print("Error: Invalid task ID. Please enter a valid ID.")
            return

        # delete task
        self.tasks.pop(task_id)

        try:
            self.save_tasks(self.file_name, self.tasks)
            print(f"Success: Task ID {task_id} deleted successfully")

        except Exception as e:
            print(f"Error deleting task. {e}")

    def do_update(self, args: str):
        """
        Command to update a task.
        Usage: update <task_id> <description>

        :param args: A single string containing the task ID and new description.
        :return:
        """

        if not args.strip():
            print("Error: Task ID and description are required")
            return

        parts = args.split(maxsplit=1)

        if len(parts) != 2:
            print("Error: Task ID & description are required\nUsage: update <task_id> <description>")
            return

        if parts[1].strip().startswith(('', "")) and len(parts[1].strip()) < 3:
            print("Error: Description cannot be empty.")
            return

        task_id, description = parts[0].strip(), parts[1].strip()

        # Load the tasks
        if not self.tasks:
            print("Error, No tasks available to update.")
            return

        # validate task ID
        if task_id not in self.tasks:
            print("Error: Invalid task ID.")
            return

        if not self.validate_task_description(self.tasks, description,
                                              'No update: The new description is identical to the current one.'): return

        # Perform update
        self.tasks[task_id]['description'] = description
        self.tasks[task_id]['updatedAt'] = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

        # save updated task
        try:
            self.save_tasks(self.file_name, self.tasks)
            print(f"Task ID {task_id} updated successfully")

        except Exception as e:
            print(f"Error saving updated task. {e}")

    def do_add(self, arg: str):
        """
        Command to add a new task.
        Usage: add <description>
        :param arg: Task description provided by user.
        """

        description = arg.strip()

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

    def validate_task_description(self, tasks: dict, des: str, msg="") -> bool:
        """
        Validates duplicate task descriptions for better task tracking.
        :param tasks: A dictionary of tasks.
        :param des: Description of task to validate.
        :param msg: Error message to be displayed.
        :return: Boolean, True on success, False on failure.
        """

        if tasks and des:
            for task in tasks.values():
                if task['description'].lower() == des.lower():
                    print("Cannot add task, task already exists") if not msg else print(msg)
                    return False

        return True
