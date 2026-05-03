tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!\n")


def show_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks available.\n")
        return

    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Pending"
        print(f"{i+1}. {t['task']} [{status}]")
    print()


def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!\n")
        else:
            print("Invalid number!\n")
    except:
        print("Enter a valid number!\n")


def mark_done():
    show_tasks()
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done!\n")
        else:
            print("Invalid number!\n")
    except:
        print("Enter a valid number!\n")


# Main loop
while True:
    print("===== TO-DO APP =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        show_tasks()
    elif ch == "3":
        delete_task()
    elif ch == "4":
        mark_done()
    elif ch == "5":
        print("Goodbye")
        break
    else:
        print("Wrong choice!\n")
