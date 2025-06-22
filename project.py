import os
import json
from tabulate import tabulate
from datetime import datetime
import pytz


task_file = "tasks.json"

INDIA_TIMEZONE = pytz.timezone('Asia/Kolkata')


# read tasks from task.json file
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as f:
            return json.load(f)
    return []


# write current list of tasks to json file
def save_tasks(tasks):
    with open(task_file, 'w') as f:
        json.dump(tasks, f, indent=4)


# adding new task to list
def add_task(title):
    tasks = load_tasks()
    task = {
        "title" : title,
        "completed" : False,
        "created_at" : datetime.now(INDIA_TIMEZONE).strftime("%Y-%m-%d %H:%M"),
        "completed_at" : None,
        "time_taken" : None
    }
    tasks.append(task)
    save_tasks(tasks)


# display all tasks in list
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No task found.")
        return

    # sort incomplete tasks first
    # tasks.sort(key=lambda task: task['completed'])

    table = []
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['completed'] else "✘"
        created = task.get('created_at', 'N/A')
        completed = task.get('completed_at', '-') if task['completed'] else '-'
        time_taken = task.get('time_taken', '-') if task['completed'] else '-'

        table.append([i, task['title'], status, created, completed, time_taken])

    headers = ['No.', 'Title', 'Completed', 'created_at', 'completed_at', 'time_taken']
    print(tabulate(table, headers= headers, tablefmt= "pretty"))


# mark a specific task complete
def mark_complete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        task = tasks[index]
        if task['completed']:
            print("Task is already completed.")
            return

        task['completed'] = True
        completed_time = datetime.now(INDIA_TIMEZONE)
        task['completed_at'] = completed_time.strftime("%Y-%m-%d %H:%M")

        created_time_naive = datetime.strptime(task['created_at'], "%Y-%m-%d %H:%M")
        created_time= INDIA_TIMEZONE.localize(created_time_naive)

        duration = completed_time - created_time
        minutes = int(duration.total_seconds() // 60)
        hours = minutes // 60
        mins = minutes % 60
        task['time_taken'] = f"{hours}h {mins}m" if hours else f"{mins}m"

        save_tasks(tasks)
        print("Task marked as completed.")
        
    else:
        print("Invalid task number.")


# delete a specific task from list
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")

    else:
        print("Invalid task number.")


def show_menu():
    print("====== SMART TO-DO ======")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task As Completed")
    print("4. Delete Task")
    print("5. Exit")


def main():

    while True:
        print()
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter task title: ").strip()
            if title:
                add_task(title)
            else:
                print("Task title can't be empty.")

        elif choice == '2':
            list_tasks()

        elif choice == '3':
            user_input = input("Enter task number to complete: ").strip()
            if user_input.isdigit():
                index = int(user_input) - 1
                mark_complete(index)
            else:
                print("Invalid input. Please enter a valid number.")

        elif choice == '4':
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Invalid input. Enter a number.")

        elif choice == '5':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
