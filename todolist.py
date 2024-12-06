# To-Do List Application in Python

# List to store tasks
tasks = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_id = int(input("\nEnter the number of the task you want to remove: "))
            if 1 <= task_id <= len(tasks):
                removed_task = tasks.pop(task_id - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                remove_task()
            elif choice == 4:
                print("\nExiting To-Do List Application. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please choose between 1 and 4.")
        except ValueError:
            print("\nPlease enter a valid number between 1 and 4.")

if __name__ == "__main__":
    main()
