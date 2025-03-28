# TaskTracker CLI

TaskTracker CLI is a Python-based command-line application designed to manage tasks efficiently. It allows users to add,
list, update, and delete tasks, with all tasks stored in a JSON file for persistence. 

Check out the [project here](https://roadmap.sh/projects/task-tracker)


## Features

- **Add Tasks**: Create tasks with a `unique ID`, `description`, and `timestamp`.
- **List Tasks**: View all tasks or filter them by status (e.g., `todo`, `in-progress`, `done`).
- **Update Tasks**: Modify task descriptions or mark their statuses.
- **Delete Tasks**: Remove tasks by their unique ID.
- **Persistent Storage**: Task data is stored in a JSON file (`tasks.json`) and loaded automatically.
- **Error Handling**: Provides user-friendly error messages and validations for all operations.

## Installation

### Prerequisites

- Python 3.7 or higher

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>


2. Navigate to the project directory.
   ```bash
   cd task-tracker-cli


### Usage
Run the application with:
 ```bash
 python index.py
```

**Commands**

1. `Add a Task`
    ```bash
    add <description>
    
    add Buy Groceries 
    ```
2. `List Tasks`
    ```bash
    list
    list <status>

    list
    list todo
   ```

3. `Update a Task`
    ```bash
    update <task_id> <description>

    Example
    update 1 Complete the assignment.
    ```
   
4. `Delete a Task`

    ```bash
    delete <task_id>

    Example
    delete 1
   ```

5. `Exit the Application`
  ```bash
  exit 
  ```

#### Advanced Usage

**Filter Tasks by Status**

`Statuses:`
- `todo`
- `in-progress`
- `done`

Example
```bash
  list done
  list in_progress
```


**Mark Task as Completed**

```bash
  mark_done 1
```


### File Details
- `TaskCLI.py`: Contains the implementation of the TaskTrackerCLI class and all the command handlers and utilities methods.
- `tasks.json`: Stores all task data persistently.


### Error Handling
- If no tasks are found the application informs the user.
- Validates task IDs and description to avoid duplication or invalid updates.
- Provides usage hints for invalid commands.



Thank you for using TaskTrackerCLI!! 😊


### CLI Interface 
![CLI Screenshot](cli-interface.png)