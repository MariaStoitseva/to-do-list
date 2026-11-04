# To-Do List

A simple command-line to-do list application built with Python.

The application allows users to add tasks, remove tasks, view active and completed tasks, and mark tasks as completed.

## Features

- Add new tasks
- Remove tasks by number
- View active tasks
- View completed tasks
- Mark tasks as completed
- Keep active and completed tasks in separate lists
- Validate task indexes
- Handle invalid numeric input
- Handle unsupported commands
- Interactive command-line interface

## Technologies

- Python
- Lists
- Loops
- Conditional logic
- Input validation

## Project Structure

```text
to-do-list/
├── to_do_list.py
└── README.md
```

## Data Structure

The application uses two lists:

```python
tasks_to_do = []
completed_tasks = []
```

Active tasks are stored in `tasks_to_do`.

Completed tasks are moved to `completed_tasks`.

## Usage

Run the application:

```bash
python to_do_list.py
```

The program accepts the following commands:

```text
add
remove
view
complete
exit
```

## Add a Task

Example:

```text
What do you want to do? add
Enter a task to add: study python
```

The task is added to the active task list.

## View Tasks

Example:

```text
What do you want to do? view
```

The application displays both active and completed tasks.

Example output:

```text
Tasks to do:
1. study python
2. finish project

Completed tasks:
1. go to the gym
```

## Complete a Task

The user selects a task by number:

```text
What do you want to do? complete
Enter the index of the task to complete: 1
```

The selected task is removed from the active list and added to the completed list.

## Remove a Task

Example:

```text
What do you want to do? remove
Enter the index of the task to remove: 2
```

The selected task is removed from the active task list.

## Validation

The application validates that:

- new tasks are not empty
- task numbers are valid integers
- task indexes exist
- negative or out-of-range indexes are rejected
- unsupported commands are rejected

## Key Concepts

This project demonstrates:

- Working with lists
- Adding and removing list elements
- Using `enumerate()`
- Converting user input to integers
- Input validation
- Exception handling with `ValueError`
- Moving data between lists
- Loops and conditional logic
- Building a basic CLI application
