import json

# Load tasks from file or initialize an empty list
def load_tasks(file_name="tasks.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks, file_name="tasks.json"):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added!")
    else:
        print("Task cannot be empty.")

# Remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Edit a task
def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to edit: "))
        new_task_name = input(f"Enter the new name for the task '{tasks[task_num - 1]['task']}': ").strip()
        if new_task_name:
            tasks[task_num - 1]["task"] = new_task_name
            print("Task updated!")
        else:
            print("Task name cannot be empty.")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()

    print("Welcome to the To-Do List App!")
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Edit a task")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()