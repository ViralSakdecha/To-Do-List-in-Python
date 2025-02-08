tasks = []

print("""
1) Add a task
2) View all tasks
3) Mark a task as done
4) Exit the To-Do list
""")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        num_task = int(input("How many tasks do you want to enter? "))

        for i in range(num_task):
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print("Task Added")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:\n")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    elif choice == "3":
        task_index = int(input("Enter the number of the task to be marked as done: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("To-Do List Exited.")
        break

    else:
        print("Enter a valid number.")
