tasks = []

def show_menu():
    print("\n<--- TO-DO LIST --->")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    num = int(input("Enter task number to complete: "))
    if 0 < num <= len(tasks):
        tasks[num-1]["done"] = True
        print(" Task marked as completed!")
    else:
        print("Invalid number.")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        removed = tasks.pop(num-1)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid number.")

while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
