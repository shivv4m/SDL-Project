import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def _init_(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        # Entry widget for adding tasks
        self.task_entry = tk.Entry(master, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for adding and marking tasks as complete
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)
        self.complete_button = tk.Button(master, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.grid(row=0, column=2, padx=5, pady=10)

        # Listbox for displaying tasks
        self.task_listbox = tk.Listbox(master, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Button for exiting the application
        self.exit_button = tk.Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=2, column=1, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_as_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            if not task.endswith(" - Completed "):
                self.tasks[index] += " - Completed✅"
                self.task_listbox.delete(index)
                self.task_listbox.insert(tk.END, self.tasks[index])
            else:
                messagebox.showinfo("Info", "Task already marked as complete.")
        else:
            messagebox.showwarning("Warning", "Please select a task.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()