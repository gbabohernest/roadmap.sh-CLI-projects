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


    def save_expense(self, filename: str, expense_obj: dict):
        """
        Save Expense to a file
        :param filename:
        :param expense_obj:
        :return:
        """

        try:
            with open(filename, 'w', encoding='utf-8') as file_obj:
                json.dump(expense_obj, file_obj, indent=4)

        except Exception as e:
            print(f"Error saving expense: {e}")


    def do_add(self, args: str):
        """
        Command to add a new expense
        Usage: add <description> <amount>
        :param args:
        :return:
        """

        if not args:
            print('Error: Please provide description and amount')
            return

        try:
            des, amount = args.strip().split(maxsplit=1)
        except ValueError:
            print("Error, Expense description and amount must be given")
            return

        if not amount.isnumeric():
            print('Error: Amount must a number')
            return

        if not int(amount) > 0:
            print('Error: Amount must be greater then zero')
            return

        exp_id = max(map(int, self.expenses.keys()), default=0) + 1 if self.expenses else 1

        expense = {
            'id': exp_id,
            'description': des,
            'amount': int(amount),
            'date': datetime.now().strftime('%Y-%m-%d  %H:%M:%S'),
            'update_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # add an expense to the expense dictionary
        self.expenses[exp_id] = expense

        # save expense to the expenses file
        self.save_expense(self.expenses_file, self.expenses)



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
