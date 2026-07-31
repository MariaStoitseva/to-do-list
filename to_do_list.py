tasks_to_do = []
completed_tasks = []

while True:
    user_choice = input("What do you want to do? add/ remove/ view/ complete/ exit ").strip().lower()

    if user_choice == "add":
        current_task = input("Enter a task to add: ").strip().lower()
        if current_task:
            tasks_to_do.append(current_task)
        else:
            print("You have to enter a valid task.")

    elif user_choice == "remove":
        try:
            tasks_number = int(input("Enter the index of the task to remove: ").strip())
            tasks_index = tasks_number - 1
            if tasks_index < 0 or tasks_index >= len(tasks_to_do):
                print("Invalid index!")
            else:
                current_task = tasks_to_do.pop(tasks_index)
                print(f"Task '{current_task}' removed.")
        except ValueError:
            print("Enter a number!")

    elif user_choice == "view":
        if tasks_to_do:
            print("Tasks to do:")
            for number, task in enumerate(tasks_to_do, start=1):
                print(f"{number}. {task}")
        else:
            print("No tasks to do")

        if completed_tasks:
            print("Completed tasks:")
            for number, task in enumerate(completed_tasks, start=1):
                print(f"{number}. {task}")
        else:
            print("No completed tasks.")

    elif user_choice == "complete":
        try:
            tasks_number = int(input("Enter the index of the task to complete: ").strip())
            tasks_index = tasks_number - 1
            if tasks_index < 0 or tasks_index >= len(tasks_to_do):
                print("Invalid index!")
            else:
                current_task = tasks_to_do.pop(tasks_index)
                completed_tasks.append(current_task)
                print(f"Task '{current_task}' completed.")
        except ValueError:
            print("Enter a number!")

    elif user_choice == "exit":
        print("Bye!")
        break
    else:
        print("Invalid input")


