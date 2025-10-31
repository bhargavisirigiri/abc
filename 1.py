import os
from datetime import datetime

class Task:
    def __init__(self, title, priority='low', due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nPriority: {self.priority}\nDue Date: {self.due_date}\nStatus: {status}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def remove(self, title):
        for task in self.tasks[:]:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def mark_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                return True
        return False

    def find(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all(self):
        return self.tasks

    def save(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title}|{task.priority}|{task.due_date}|{task.completed}\n")

    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    title, priority, due_date, completed = line.strip().split('|')
                    due_date = datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None
                    completed = completed == 'True'
                    task = Task(title, priority, due_date, completed)
                    self.add(task)

def initiate():
    filename = "tasks.txt"
    todo_list = ToDoList()
    todo_list.load(filename)

    while True:
        print("\n1. Add New Task")
        print("2. Remove a Task")
        print("3. Mark Task as Completed")
        print("4. Show All Tasks")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Priority (high/medium/low): ")
            while priority.lower() not in ['high', 'medium', 'low']:
                print("Invalid priority. Please choose 'high', 'medium', or 'low'.")
                priority = input("Priority (high/medium/low): ")
            due_date_str = input("Due date (YYYY-MM-DD), press enter if none: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
            task = Task(title, priority, due_date)
            todo_list.add(task)
            todo_list.save(filename)
            print("Task added.")

        elif choice == '2':
            title = input("Enter task title to remove: ")
            if todo_list.remove(title):
                todo_list.save(filename)
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            if todo_list.mark_done(title):
                todo_list.save(filename)
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == '4':
            tasks = todo_list.get_all()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks.")

        elif choice == '5':
            confirmation = input("Are you sure you want to clear all tasks? (yes/no): ")
            if confirmation.lower() == 'yes':
                todo_list.tasks = []  
                todo_list.save(filename)
                print("All tasks cleared.")
            else:
                print("Operation canceled.")

        elif choice == '6':
            print("Exited.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    initiate()
