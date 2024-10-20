import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("400x300")
        
        self.tasks = []
                                            
        # Create GUI elements
        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        self.complete_button = tk.Button(self.master, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, f"✓ {task}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")
    
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()

