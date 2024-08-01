def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(filename, tasks)
        elif choice == '2':
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
