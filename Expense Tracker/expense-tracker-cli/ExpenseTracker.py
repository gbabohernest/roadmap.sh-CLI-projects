"""
This module contains the ExpenseTracker, a cli too for managing your expenses.
"""

import os
import json
import cmd
from datetime import datetime
from json import JSONDecodeError
from time import strptime


class ExpenseTracker(cmd.Cmd):
    """
    The command-line interface for tracking expenses.
    """
    intro = 'Welcome to ExpenseTracker CLI Tool.\nType help or ? to list commands.\n'
    prompt = 'expense-tracker -> '
    expenses_file = 'expenses.json'

    def __init__(self):
        super().__init__()
        self.expenses = self.load_expenses(self.expenses_file)

    def load_expenses(self, file: str) -> dict:
        """
        Loads expenses from storage
        :param file: file containing expenses.
        :return: A dict containing expenses or an empty dict
        """

        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as file_obj:
                    return json.load(file_obj)
            except JSONDecodeError:
                print('Error, unable to load expenses.')

        return {}

    def save_expenses(self, filename: str, expense_obj: dict):
        """
        Save Expense to a JSON file.
        :param filename: The name of the file.
        :param expense_obj: A dict containing expenses.
        """

        try:
            with open(filename, 'w', encoding='utf-8') as file_obj:
                json.dump(expense_obj, file_obj, indent=4)

        except Exception as e:
            print(f"Error saving expenses: {e}")

    def save_expense_operations(self, expense_id: str, msg: str):
        """
         Saves changes to an expense into the JSON file and displays a status message.
        :param expense_id: The ID of the expense being modified.
        :param msg: A success message describing the operation performed.
        """

        try:
            self.save_expenses(self.expenses_file, self.expenses)
            print(f"Success: Expense with ID {expense_id} {msg}.")

        except Exception as e:
            print(f"Error saving expense operation. {e}")

    def do_add(self, args):
        """
        Command to add a new expense.
        Usage: add <description> <amount>
        """
        try:
            description, amount = args.split(maxsplit=1)
        except ValueError:
            print("Error: Invalid input. Use 'add <description> <amount>'.")
            return

        description = description.strip()
        amount = amount.strip()

        if not self.validate_expense_description(self.expenses, description):
            return

        if not self.validate_expense_amount(amount):
            return

        expense_id = max(map(int, self.expenses.keys()), default=0) + 1 if self.expenses else 1
        expense = {
            'id': expense_id,
            'description': description,
            'amount': float(amount.strip()),
            'date': datetime.now().strftime('%b-%d-%Y  %I:%M %p'),
        }
        self.expenses[str(expense_id)] = expense
        self.save_expense_operations(str(expense_id), 'added successfully')

    def do_list(self, _):
        """
        Command to list all expenses.
        """
        if not self.check_expenses_dict('list'):
            return

        print(f"{'ID':<5} {'Date':<30} {'Updated':30} {'Description':<20} {'Amount':<10}")
        print("-" * 100)
        for expense in self.expenses.values():
            print(
                f"{expense['id']:<5} {expense['date']:<30} {expense.get('updated', '--------'):<30} {expense['description']:<20} ${(expense['amount']):.2f}")

    def do_delete(self, arg):
        """
        Command to delete an existing expense.
        Usage: delete <id>
        :param arg: Expense ID
        """

        if not self.check_expenses_dict('delete'):
            return
        try:
            expense_id = arg.strip()

        except ValueError:
            print('Error: Invalid input. Use "delete <id>". ')
            return

        expense_id = expense_id.strip()

        if not self.validate_expense_id(self.expenses, expense_id):
            return

        del self.expenses[expense_id]

        self.save_expense_operations(expense_id, 'deleted successfully')

    def do_update(self, args):
        """
        Command to update an existing expense.
        Usage: update <id> <description> <amount>
        """

        try:
            expense_id, description, amount = args.split(maxsplit=2)
        except ValueError:
            print("Error: Invalid input. Use 'update <id> <description> <amount>'.")
            return

        if not self.check_expenses_dict('update'):
            return

        expense_id = expense_id.strip()
        description = description.strip()
        amount = amount.strip()

        if not self.validate_expense_id(self.expenses, expense_id):
            return

        if not self.validate_expense_description(self.expenses, description,
                                                 'No update: The new description is the same as the current description.'):
            return

        if not self.validate_expense_amount(amount):
            return

        self.expenses[expense_id].update({
            'description': description,
            'amount': float(amount),
            'updated': datetime.now().strftime('%b-%d-%Y  %I:%M %p'),
        })

        self.save_expense_operations(expense_id, 'updated successfully')

    def do_summary(self, arg):
        """
        Command to show a summary of all expenses or for a particular month.
        Usage: summary |  summary <month>
        :param arg: The month in number (1-12). Example: summary 8
        """

        if not self.check_expenses_dict('summarize'):
            return

        all_expenses = self.expenses.values()

        months = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }

        if arg:

            try:
                filter_month = int(arg.strip())
            except ValueError:
                print('Error: Month should be a number')
                return

            if not (1 <= filter_month <= 12):
                print(f"Error: Month should between 1 - 12")
                return

            filtered_expenses = [
                expense['amount'] for expense in all_expenses if
                datetime.strptime(expense['date'].split()[0], '%b-%d-%Y').month == filter_month
            ]

            if not filtered_expenses:
                print(f"NO Expenses recorded for {months[filter_month]}")

            else:
                total_expense = sum(filtered_expenses)
                print(f"Total expense for {months[filter_month]}: ${total_expense:.2f}")

        else:
            total_expense = sum(expense['amount'] for expense in all_expenses)
            print(f"Total expenses: ${total_expense:.2f}")

    def check_expenses_dict(self, command: str):
        """
        check if the expenses dict is empty or not
        :param command:
        :return: Boolean, if expense return True, otherwise false.
        """

        if not self.expenses:
            print(f'Error: No expenses recorded to {command}, add an expense.')
            return False

        return True

    def validate_expense_id(self, expenses: dict, expense_id: str) -> bool:
        """
        Validate if an expense ID exists.
        :param expenses: A dict of all expenses.
        :param expense_id: Expense ID
        :return: Return True if valid false otherwise.
        """

        if expense_id not in expenses:
            print(f"Error: Expense ID {expense_id} not found.")
            return False

        return True

    def validate_expense_description(self, expenses: dict, description: str, msg='') -> bool:
        """
        Validate the expense description
        :param expenses: A dict containing expenses.
        :param description: Expense description
        :param msg: Error message to be displayed.
        :return: Boolean, True on success, False on failure.
        """

        if expenses is not None:
            for expense in expenses.values():
                if expense['description'].lower() == description.lower():
                    # duplicate, or expense already exists.
                    print("Error! Cannot Add Expense, Expense already exits.") if not msg else print(msg)
                    return False

            return True

    def validate_expense_amount(self, amount: str) -> bool:
        """
        Validate the expense amount.
        :param amount: The amount
        :return: Return True if amount is valid, otherwise false.
        """
        try:
            amount = float(amount)

            if amount <= 0:
                print("Invalid: Amount must be greater than zero!")
                return False

            return True

        except ValueError:
            print("Invalid: Amount must be a number!")

        return False

    def do_EOF(self, arg) -> bool:
        """
        Command to exits the application when EOF signal is received.
        Usage: EOF (Ctrl+D)
        """
        print("")
        return True

    def do_exit(self, arg):
        """
        Command Exit the application.
        """
        return True
