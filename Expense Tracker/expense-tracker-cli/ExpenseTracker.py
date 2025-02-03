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
    prompt = 'expense-tracker -> '
    expenses_file = 'expenses.json'

    def __init__(self):
        super().__init__()
        self.expenses = self.load_expenses(self.expenses_file)

    def do_update(self, args):
        """
        Command to update an existing expense.
        Usage: update <id> <description> <amount>
        """

        try:
            expense_id, description, amount = args.split(maxsplit=2)
            expense_id = str(expense_id)
            amount = float(amount)
            if expense_id not in self.expenses:
                raise KeyError("Expense ID not found.")
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        except (ValueError, KeyError):
            print("Error: Invalid input. Use 'update <id> <description> <amount>'.")
            return

        self.expenses[expense_id].update({
            'description': description,
            'amount': amount,
            'date': datetime.now().strftime('%Y-%m-%d'),
        })
        self.save_expenses()
        print(f"Expense with ID {expense_id} updated successfully.")

    def do_delete(self, args):
        """
        Command to delete an expense.
        Usage: delete <id>
        """

        ## still need working
        try:
            expense_id = args.strip()
            if expense_id:
                if expense_id not in self.expenses:
                    raise KeyError("Expense ID not found.")
        except KeyError:
            print("Error: Invalid input. Use 'delete <id>'.")
            return

        del self.expenses[expense_id]
        # self.save_expenses()
        self.save_expense_operations(expense_id, 'deleted successfully')

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
            print(f"Error marking the status. {e}")

    def save_expenses(self, filename: str, expense_obj: dict):
        """
        Save Expense to a file
        :param filename: The name of the file.
        :param expense_obj: A dict containing expenses.
        """

        try:
            with open(filename, 'w', encoding='utf-8') as file_obj:
                json.dump(expense_obj, file_obj, indent=4)

        except Exception as e:
            print(f"Error saving expense: {e}")

    def do_add(self, args):
        """
        Command to add a new expense.
        Usage: add <description> <amount>
        """
        try:
            description, amount = args.split(maxsplit=1)

            if not self.validate_expense_description(self.expenses, description):
                return
            if not self.validate_expense_amount(amount):
                return

        except ValueError:
            print("Error: Invalid input. Use 'add <description> <amount>'.")
            return

        expense_id = max(map(int, self.expenses.keys()), default=0) + 1 if self.expenses else 1
        expense = {
            'id': expense_id,
            'description': description,
            'amount': amount,
            'date': datetime.now().strftime('%Y-%m-%d'),
        }
        self.expenses[str(expense_id)] = expense
        self.save_expense_operations(str(expense_id), 'added successfully')

    def validate_expense_description(self, expenses: dict,  description: str) -> bool:
        """
        Validate the expense description
        :param expenses: A dict containing expenses.
        :param description: Expense description
        :return:
        """

        if expenses and description:
            for expense in expenses.values():
                if expense['description'].lower() == description.lower():
                    # duplicate, or expense already exists.
                    print("Error! Cannot Add Expense, Expense already exits.")
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
