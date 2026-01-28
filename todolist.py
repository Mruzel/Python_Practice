import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"

# ---------------- Functions ---------------- #

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    save_tasks()


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


# ---------------- GUI Setup ---------------- #

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 18, "bold")
).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(fill="x", padx=20, pady=10)

tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    width=15,
    command=add_task
).pack(pady=5)

task_listbox = tk.Listbox(
    root,
    font=("Arial", 12),
    height=12
)
task_listbox.pack(fill="both", padx=20, pady=10, expand=True)

tk.Button(
    root,
    text="Delete Selected Task",
    font=("Arial", 12),
    width=20,
    command=delete_task
).pack(pady=5)

# Load tasks when app starts
load_tasks()

root.mainloop()
