"""
Simple To-Do List Application
Manage your daily tasks with add, view, complete, and delete features.
Uses loops for menu navigation and list operations.
"""

def display_menu():
    print("\n" + "="*40)
    print("📝 TO-DO LIST MANAGER")
    print("="*40)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Clear all tasks")
    print("6. Exit")
    print("="*40)

def view_tasks(tasks):
    if not tasks:
        print("\n✨ No tasks yet! You're all caught up.")
        return
    
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "⭕"
        print(f"{i}. {status} {task['title']}")

def add_task(tasks):
    title = input("\nEnter task description: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print(f"✅ Added: {title}")
    else:
        print("❌ Task cannot be empty!")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print(f"✅ Completed: {tasks[index]['title']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ Deleted: {deleted['title']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def clear_all(tasks):
    confirm = input("\n⚠️ Delete ALL tasks? (yes/no): ").lower()
    if confirm in ['yes', 'y']:
        tasks.clear()
        print("🗑️ All tasks cleared!")
    else:
        print("Cancelled.")

def main():
    tasks = []
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            clear_all(tasks)
        elif choice == '6':
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("❌ Invalid option! Please choose 1-6.")

if __name__ == "__main__":
    main()