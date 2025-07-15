import tkinter as tk
from tkinter import messagebox
import json
import os




class TodoApp:
  def __init__(self, root):
      self.root = root
      self.root.title("To-Do List")
      self.root.geometry("400x500")
      self.tasks = []
      self.file_path = "tasks.json"
      self.load_tasks()




      # GUI Elements
      self.task_entry = tk.Entry(self.root, width=40)
      self.task_entry.pack(pady=10)




      self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
      self.add_button.pack(pady=5)




      self.task_listbox = tk.Listbox(self.root, width=40, height=15)
      self.task_listbox.pack(pady=10)




      self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.complete_task)
      self.complete_button.pack(pady=5)




      self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
      self.delete_button.pack(pady=5)




      self.update_listbox()




  def load_tasks(self):
      if os.path.exists(self.file_path):
          try:
              with open(self.file_path, 'r') as file:
                  self.tasks = json.load(file)
          except json.JSONDecodeError:
              self.tasks = []
      else:
          self.tasks = []




  def save_tasks(self):
      with open(self.file_path, 'w') as file:
          json.dump(self.tasks, file, indent=4)




  def add_task(self):
      task_text = self.task_entry.get().strip()
      if task_text:
          self.tasks.append({"task": task_text, "completed": False})
          self.save_tasks()
          self.update_listbox()
          self.task_entry.delete(0, tk.END)
      else:
          messagebox.showwarning("Warning", "Task cannot be empty!")




  def update_listbox(self):
      self.task_listbox.delete(0, tk.END)
      for idx, task in enumerate(self.tasks, 1):
          status = "✓" if task["completed"] else " "
          self.task_listbox.insert(tk.END, f"{idx}. [{status}] {task['task']}")




  def complete_task(self):
      try:
          selected = self.task_listbox.curselection()[0]
          self.tasks[selected]["completed"] = True
          self.save_tasks()
          self.update_listbox()
      except IndexError:
          messagebox.showwarning("Warning", "Please select a task!")




  def delete_task(self):
      try:
          selected = self.task_listbox.curselection()[0]
          self.tasks.pop(selected)
          self.save_tasks()
          self.update_listbox()
      except IndexError:
          messagebox.showwarning("Warning", "Please select a task!")


def main():
  root = tk.Tk()
  app = TodoApp(root)
  root.mainloop()


# This code is a simple To-Do List application using Tkinter and JSON for storage.
if __name__ == "__main__":
  main()
