import os

def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        file.write("\n".join(tasks))

def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)

def remove_task(index, tasks):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

tasks = load_tasks()
while True:
    action = input("Enter 'add', 'remove', 'list', or 'exit': ").lower()
    if action == "add":
        task = input("Enter task: ")
        add_task(task, tasks)
    elif action == "remove":
        index = int(input("Enter task index to remove: "))
        remove_task(index, tasks)
    elif action == "list":
        for i, task in enumerate(tasks):
            print(f"{i}: {task}")
    elif action == "exit":
        break
    else:
        print("Invalid action")
