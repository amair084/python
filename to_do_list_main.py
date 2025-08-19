import sqlite3
import tkinter as tk
from tkinter import messagebox
import os

from tkinter import PhotoImage

# --- Ensure database file is created ---
import os

# Get the folder where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create database path in the same folder as the script
DB_FILE = os.path.join(script_dir, "todo.db")

print(f"Database will be created in: {os.path.abspath(DB_FILE)}")

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
""")
conn.commit()
conn.close()


# --- Database functions ---
def add_task(description):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def get_completed_count():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_total_count():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# --- GUI Functions ---
def refresh_tasks():
    task_list.delete(0, tk.END)
    global task_id_map
    task_id_map = {}
    tasks = get_tasks()
    for display_idx, task in enumerate(tasks, start=1):
        task_id, desc, completed = task
        task_id_map[display_idx] = task_id
        status = "✔" if completed else "✖"
        task_list.insert(tk.END, f"{display_idx}: {desc} [{status}]")
        color = "green" if completed else "red"
        task_list.itemconfig(tk.END, {'fg': color})
    # Update the counter label
    completed = get_completed_count()
    total = get_total_count()
    counter_label.config(text=f"Completed: {completed} / {total}")

def add_task_gui():
    desc = task_entry.get()
    if desc.strip():
        add_task(desc)
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task_gui():
    selection = task_list.curselection()
    if selection:
        display_idx = selection[0] + 1  # listbox is 0-indexed
        db_id = task_id_map[display_idx]
        delete_task(db_id)
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def complete_task_gui():
    selection = task_list.curselection()
    if selection:
        display_idx = selection[0] + 1
        db_id = task_id_map[display_idx]
        complete_task(db_id)
        refresh_tasks()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")


# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x450")
root.configure(bg="#0F0F0F")

counter_label = tk.Label(root, text="", font=("Helvetica", 10, "bold"), bg="#383838", fg ="white")
counter_label.pack(pady=15)
logo_path = os.path.join(script_dir, "logo.png")


if os.path.exists(logo_path):
    from PIL import Image, ImageTk, ImageDraw # type: ignore
    original_image = Image.open(logo_path).convert("RGBA")
    resized_image = original_image.resize((75, 75), Image.Resampling.LANCZOS)

    mask = Image.new("L", (75, 75), 0)  # L = greyscale (mask)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 75, 75), fill=255)  # white circle

    resized_image.putalpha(mask)

    logo_img = ImageTk.PhotoImage(resized_image)

    logo_label = tk.Label(root, image=logo_img, bg="#0F0F0F")
    logo_label.pack(side="top", anchor="ne", padx=10, pady=10)

    icon_path = os.path.join(script_dir, "my_icon.png")  # or .ico

    if os.path.exists(icon_path):
        icon_image = ImageTk.PhotoImage(file=icon_path)
        root.iconphoto(False, icon_image)

task_entry = tk.Entry(root, width=40, font=("Helvetica", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", bg="#142A4B", fg="white",
                       font=("Helvetica", 10, "bold"), command=add_task_gui)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Complete", bg="#083808", fg="white",
                            font=("Helvetica", 10, "bold"), command=complete_task_gui)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", bg="#f44336", fg="white",
                          font=("Helvetica", 10, "bold"), command=delete_task_gui)
delete_button.pack(pady=5)

task_list = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12), fg="red")
task_list.pack(pady=10)

# --- Task ID mapping for proper deletion/completion ---
task_id_map = {}

refresh_tasks()
root.mainloop()