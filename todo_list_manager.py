import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n✅ Your to-do list is empty!\n")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("✅ Task added!\n")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if tasks[index].startswith("[ ]"):
            tasks[index] = tasks[index].replace("[ ]", "[x]", 1)
            save_tasks(tasks)
            print("✅ Task marked as complete!\n")
        else:
            print("⚠️ Task is already complete.\n")
    except (IndexError, ValueError):
        print("❌ Invalid task number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed}\n")
    except (IndexError, ValueError):
        print("❌ Invalid task number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("📌 To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()