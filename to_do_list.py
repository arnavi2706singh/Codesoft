import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 To-Do List Manager")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Task storage
        self.tasks = []
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="📋 TO-DO LIST MANAGER", 
                              font=("Arial", 20, "bold"), 
                              bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')
        
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=40)
        self.task_entry.pack(side='left', padx=(0, 10), fill='x', expand=True)
        self.task_entry.bind('<Return>', lambda event: self.add_task())
        
        add_button = tk.Button(input_frame, text="➕ Add Task", 
                              command=self.add_task, 
                              font=("Arial", 10, "bold"),
                              bg='#3498db', fg='white',
                              padx=20, pady=5)
        add_button.pack(side='right')
        
        # Task list frame
        list_frame = tk.Frame(self.root, bg='#f0f0f0')
        list_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Task listbox
        self.task_listbox = tk.Listbox(list_frame, 
                                      font=("Arial", 11),
                                      yscrollcommand=scrollbar.set,
                                      selectmode='single',
                                      height=15,
                                      bg='white',
                                      selectbackground='#e8f4fd')
        self.task_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10, padx=20, fill='x')
        
        # Buttons
        mark_done_btn = tk.Button(button_frame, text="✅ Mark Done", 
                                 command=self.mark_done,
                                 font=("Arial", 10, "bold"),
                                 bg='#27ae60', fg='white',
                                 padx=15, pady=5)
        mark_done_btn.pack(side='left', padx=5)
        
        mark_undone_btn = tk.Button(button_frame, text="↩️ Mark Undone", 
                                   command=self.mark_undone,
                                   font=("Arial", 10, "bold"),
                                   bg='#f39c12', fg='white',
                                   padx=15, pady=5)
        mark_undone_btn.pack(side='left', padx=5)
        
        edit_btn = tk.Button(button_frame, text="✏️ Edit Task", 
                            command=self.edit_task,
                            font=("Arial", 10, "bold"),
                            bg='#9b59b6', fg='white',
                            padx=15, pady=5)
        edit_btn.pack(side='left', padx=5)
        
        delete_btn = tk.Button(button_frame, text="🗑️ Delete Task", 
                              command=self.delete_task,
                              font=("Arial", 10, "bold"),
                              bg='#e74c3c', fg='white',
                              padx=15, pady=5)
        delete_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(button_frame, text="🧹 Clear Completed", 
                             command=self.clear_completed,
                             font=("Arial", 10, "bold"),
                             bg='#34495e', fg='white',
                             padx=15, pady=5)
        clear_btn.pack(side='right', padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                             relief='sunken', anchor='w',
                             bg='#ecf0f1', fg='#2c3e50')
        status_bar.pack(side='bottom', fill='x')
        
        # Update display
        self.update_display()
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_display()
            self.status_var.set(f"✅ Task '{task_text}' added successfully!")
            self.root.after(3000, lambda: self.status_var.set("Ready"))
        else:
            messagebox.showwarning("Warning", "Please enter a task description!")
    
    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            if not self.tasks[index]["done"]:
                self.tasks[index]["done"] = True
                self.update_display()
                self.status_var.set("🎉 Task marked as done!")
                self.root.after(3000, lambda: self.status_var.set("Ready"))
            else:
                messagebox.showinfo("Info", "Task is already completed!")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")
    
    def mark_undone(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            if self.tasks[index]["done"]:
                self.tasks[index]["done"] = False
                self.update_display()
                self.status_var.set("↩️ Task marked as undone!")
                self.root.after(3000, lambda: self.status_var.set("Ready"))
            else:
                messagebox.showinfo("Info", "Task is already pending!")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as undone!")
    
    def edit_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            current_task = self.tasks[index]["task"]
            new_task = simpledialog.askstring("Edit Task", "Enter new task description:", 
                                             initialvalue=current_task)
            if new_task and new_task.strip():
                self.tasks[index]["task"] = new_task.strip()
                self.update_display()
                self.status_var.set("✏️ Task updated successfully!")
                self.root.after(3000, lambda: self.status_var.set("Ready"))
        else:
            messagebox.showwarning("Warning", "Please select a task to edit!")
    
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.tasks[index]["task"]
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete:\n'{task_text}'?"):
                self.tasks.pop(index)
                self.update_display()
                self.status_var.set(f"🗑️ Task '{task_text}' deleted!")
                self.root.after(3000, lambda: self.status_var.set("Ready"))
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def clear_completed(self):
        completed_tasks = [t for t in self.tasks if t["done"]]
        if completed_tasks:
            if messagebox.askyesno("Confirm Clear", f"Delete {len(completed_tasks)} completed task(s)?"):
                self.tasks = [t for t in self.tasks if not t["done"]]
                self.update_display()
                self.status_var.set(f"🧹 {len(completed_tasks)} completed task(s) cleared!")
                self.root.after(3000, lambda: self.status_var.set("Ready"))
        else:
            messagebox.showinfo("Info", "No completed tasks to clear!")
    
    def update_display(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✅" if task["done"] else "❌"
            display_text = f"{status} {task['task']}"
            self.task_listbox.insert(tk.END, display_text)
            
            # Color coding for completed tasks
            if task["done"]:
                self.task_listbox.itemconfig(i, {'fg': '#7f8c8d'})
        
        # Update window title with task count
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["done"])
        self.root.title(f"📋 To-Do List Manager ({completed_tasks}/{total_tasks})")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (600 // 2)
    y = (root.winfo_screenheight() // 2) - (500 // 2)
    root.geometry(f"600x500+{x}+{y}")
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()