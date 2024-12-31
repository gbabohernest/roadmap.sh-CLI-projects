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

    def do_list(self, arg):
        """
        Command to list all tasks, optionally filtered by status.
        Usage:
        - list                 # Lists all tasks.
        - list <status>        # Lists tasks filtered by status.
                               # Valid statuses: todo, in-progress, done.
        :param arg: The status to filter tasks by, or empty to list all tasks.
        """

        if arg:
            arg = arg.strip().lower()

            valid_statuses = {'done': 'done', 'todo': 'todo', 'in_progress': 'in-progress'}
            status = valid_statuses.get(arg)

            if status:
                if not self.retrieve_tasks_list(status): return

            else:
                print("Error: Invalid status provided.\nUsage: list <done>\nlist <in_progress>\nlist <todo>")
                return

        else:
            # List all tasks.
            if not self.retrieve_tasks_list(): return

    def do_mark_done(self, arg: str):
        """
        Command to mark task status (done)
        Usage: mark_done <task_id>
        :param arg: Task ID
        """
        if not self.validate_task_id(arg, self.tasks, 'mark-done'): return

        task_id = arg.strip()

        # mark task as done
        self.tasks[task_id]['status'] = 'done'

        # save changes to task back into the file.
        self.save_task_operations(task_id, 'status marked as done')

    def do_mark_in_progress(self, arg: str):
        """
        Command to mark task status (in-progress)
        Usage: mark_in_progress <task_id>
        :param arg: Task ID.
        """

        if not self.validate_task_id(arg, self.tasks, 'mark-in-progress'): return

        task_id = arg.strip()

        # mark task as in progress
        self.tasks[task_id]['status'] = 'in-progress'

        # save changes to task back into the file.
        self.save_task_operations(task_id, 'status marked as in-progress')

    def do_delete(self, arg: str):
        """
        Command to delete a task.
        Usage: delete <task_ID>
        :param arg: ID of the task to delete.
        """

        if not self.validate_task_id(arg, self.tasks, 'delete'): return

        task_id = arg.strip()

        # delete task
        self.tasks.pop(task_id)

        # save changes to task back into the file.
        self.save_task_operations(task_id, 'deleted successfully')

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
        self.save_task_operations(task_id, 'updated successfully')

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

        # save task
        self.save_task_operations(str(task_id), 'added successfully.')

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

    def validate_task_id(self, task_id: str, tasks: dict, command: str) -> bool:
        """
         Validates the task ID provided by the user.

         This function checks whether the given task ID is valid for operations such as marking
         a task's status.

         :param task_id: The ID of the task as a string.
         :param tasks: A dictionary containing existing tasks with task IDs as keys.
         :param command: A string denoting the command's name
         :return:
             - True if the task ID is valid and exists in the task dictionary.
             - False if any validation step fails, with an appropriate error message.
         """

        task_id = task_id.strip()

        if not task_id:
            print(f"Error: Please provide the ID of the task.\nUsage: {command} <task_ID>.")
            return False

        if not tasks:
            print("Error: No tasks available to mark status. Add tasks")
            return False

        if task_id not in tasks:
            print("Error: Invalid task ID. Please enter a valid ID.")
            return False

        return True

    def save_task_operations(self, task_id: str, msg: str):
        """
         Saves changes to a task into the JSON file and displays a status message.
        :param task_id: The ID of the task being modified.
        :param msg: A success message describing the operation performed.
        """

        try:
            self.save_tasks(self.file_name, self.tasks)
            print(f"Success: Task with ID {task_id} {msg}.")

        except Exception as e:
            print(f"Error marking the status. {e}")

    def retrieve_tasks_list(self, ops="") -> bool:
        """
       Retrieves and displays tasks, optionally filtered by status.

       :param ops: The status to filter tasks by (e.g., "done", "todo", "in-progress").
                   If empty, all tasks are listed.

       :returns bool: True if tasks are successfully listed, False otherwise.
        """

        if not self.tasks:
            print("Sorry no tasks to load. Try adding a task.")
            return False

        # filter task based on `ops` if provided.
        filtered_tasks = {k: v for k, v in self.tasks.items() if not ops or v['status'] == ops}

        if not filtered_tasks:
            print(f"No tasks found with status `{ops}`")
            return False

        print(f"{'Task ID':<10} {'Description':<30} {'Status':<20} {'Created At':<30} {'Updated At':<30}")
        print("=" * 130)

        for key, value in filtered_tasks.items():
            print(
                f"{key:<10} {value['description']:<30} {value['status']:<20}"
                f"{value['createdAt']:<30} {value['updatedAt']:<30}")

        return True
