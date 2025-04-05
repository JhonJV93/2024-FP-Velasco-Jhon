import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        self.tasks = []

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.add_task)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.root.bind('<c>', self.complete_task)
        self.root.bind('<C>', self.complete_task)
        self.root.bind('<d>', self.delete_task)
        self.root.bind('<D>', self.delete_task)
        self.root.bind('<Escape>', lambda event: root.quit())

    def add_task(self, event=None):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({'text': task_text, 'completed': False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese una tarea.")

    def complete_task(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_task_list()

    def delete_task(self, event=None):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['text']
            if task['completed']:
                display_text += " [Completada]"
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
