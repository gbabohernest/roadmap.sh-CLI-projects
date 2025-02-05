# Expense Tracker CLI App

## Overview
The Expense Tracker is a simple command-line application to help you manage your finances. It allows you to add, update,
delete, and view your expenses, along with providing summaries to give you insights into your spending habits.

## Features 
 - Add Expenses: Add an expense with a description and amount.
 - Update Expenses: Modify existing expenses using its ID.
 - Delete Expenses: Remove an expense using its ID.
 - View All Expenses: List all expenses with their details.
 - Summary: Summarize expenses for a specific month or all time.
 - Persistent storage using JSON


## Installation

1. Clone the Repository

    ```Bash
    git clone <resposity url>
    cd ExpenseTracker/expense-tracker-cli
    ```

2. Run the Script 
   - Make sure you have python 3.10+ installed.
   ```Bash
   python index.py
   - ```

## Usage
Once inside the CLI, use the commands below to manage your expenses.

 - `Add an Expense`
    ```Bash
    add Lunch 10.50
    ```
 
- `List all Expenses`
 ```Bash
    list 
   ```

 - `Update an Expense`
 ```Bash
    update 1 Dinner 15
 ```


 - `Delete an Expense`
 ```Bash
    delete 1
 ```

- `View Summary of Expenses`
  - All-time total
     ```Bash
    summary
     ```

  - For a specific month
 ```Bash
    summary 2
 ```

- Exit the CLI
 ```Bash
    exit
 ```
 or 
 ```Bash
    Ctrl + D
 ```