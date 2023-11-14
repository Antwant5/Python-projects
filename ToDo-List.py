tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully")

def remove_task():
    if len(tasks) == 0:
        print("No tasks to delete")
    else:
        print("Tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i + 1}, {task}")
        choice = int(input("Enter number of task you want to delete: "))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully")
        else:
            print("Invalid task number")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("list of tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i + 1}, {task}")

def main():
    while True:
        print("\n******** To-Do-List App ********")
        print("1. Add task")
        print("2. Remove task")
        print("3. View task")
        print("4. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            print("Thank you for using the To-Do-List app")
            break
        else:
            print("Invalid choice try again")


if __name__ == '__main__':
    main()