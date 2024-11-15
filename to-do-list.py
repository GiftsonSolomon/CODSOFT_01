# Simple To-Do List Application

todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
        return
    
    print("\n--- To-Do List ---")
    for index, task in enumerate(todo_list, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def mark_task_complete():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
