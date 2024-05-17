tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print("Task not found")

def show_tasks():
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks available")

def main():
    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
