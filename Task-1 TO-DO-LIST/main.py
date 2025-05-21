import tkinter as tk
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.tasks = {}

        # Entry field
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.create_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_task_completed)
        self.complete_button.pack(pady=5)

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, status in self.tasks.items():
            status_str = "✓" if status else "✗"
            self.task_listbox.insert(tk.END, f"{task} [{status_str}]")

    def create_task(self):
        task_name = self.task_entry.get()
        if task_name:
            if task_name not in self.tasks:
                self.tasks[task_name] = False
                self.refresh_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Task already exists!")

    def update_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            old_task = self.task_listbox.get(selected).split(' [')[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[new_task] = self.tasks.pop(old_task)
                self.refresh_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Enter new task name!")
        else:
            messagebox.showerror("Error", "Select a task to update!")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_name = self.task_listbox.get(selected).split(' [')[0]
            del self.tasks[task_name]
            self.refresh_listbox()
        else:
            messagebox.showerror("Error", "Select a task to delete!")

    def mark_task_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            task_name = self.task_listbox.get(selected).split(' [')[0]
            self.tasks[task_name] = True
            self.refresh_listbox()
        else:
            messagebox.showerror("Error", "Select a task to mark completed!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
