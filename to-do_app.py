import os

file = "tasks.txt"

def loadTasks():
    tasks = []
    if os.path.exists(file):
        f = open(file, "r")
        for line in f:
            tasks.append(line.strip())
        f.close()
    return tasks


def saveTasks(tasks):
    f = open(file, "w")
    for t in tasks:
        f.write(t + "\n")
    f.close()


def addTask(tasks):
    t = input("Enter task: ")
    tasks.append(t)
    saveTasks(tasks)
    print("Task added\n")


def showTasks(tasks):
    if len(tasks) == 0:
        print("No tasks\n")
        return
    
    print("Tasks:")
    i = 1
    for t in tasks:
        print(i, "-", t)
        i += 1
    print()


def deleteTask(tasks):
    showTasks(tasks)
    n = int(input("Enter number: "))
    
    if n > 0 and n <= len(tasks):
        tasks.pop(n-1)
        saveTasks(tasks)
        print("Deleted\n")
    else:
        print("Invalid\n")


def markDone(tasks):
    showTasks(tasks)
    n = int(input("Enter number: "))
    
    if n > 0 and n <= len(tasks):
        tasks[n-1] = tasks[n-1] + " (done)"
        saveTasks(tasks)
        print("Updated\n")
    else:
        print("Invalid\n")


tasks = loadTasks()

while True:
    print("1 Add")
    print("2 Show")
    print("3 Delete")
    print("4 Done")
    print("5 Exit")

    ch = input("Choice: ")

    if ch == "1":
        addTask(tasks)
    elif ch == "2":
        showTasks(tasks)
    elif ch == "3":
        deleteTask(tasks)
    elif ch == "4":
        markDone(tasks)
    elif ch == "5":
        break
    else:
        print("Wrong choice\n")