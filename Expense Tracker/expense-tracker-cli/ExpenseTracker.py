"""
This module contains the ExpenseTracker, a cli too for managing your expenses.
"""

import os
import json
import cmd
from datetime import datetime
from json import JSONDecodeError


class ExpenseTracker(cmd.Cmd):
    """
    The command-line interface for tracking expenses.
    """
    intro = 'Welcome to ExpenseTracker CLI Tool.\nType help or ? to list commands.\n'
    prompt = 'expense-tracker ->'
    expenses_file = 'expenses.json'

    def __init__(self):
        super().__init__()
        self.expenses = self.load_expenses(self.expenses_file)

    def load_expenses(self, file: str) -> dict:
        """
        Loads expenses from storage
        :param file:
        :return:
        """

        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as file_obj:
                    return json.load(file_obj)
            except JSONDecodeError:
                print('Error, unable to load expenses.')

        return {}

    def do_EOF(self, arg) -> bool:
        """
        Command to exits the application when EOF signal is received.
        Usage: EOF (Ctrl+D)
        """
        print("")
        return True
