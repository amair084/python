## Repeatable Action Counter

import sqlite3
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import PhotoImage

# Get Folder for DB and Create it
script_directory = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(script_directory, "action_counter.db")

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    count INTEGER DEFAULT 0        
               )
               """)
conn.commit()
conn.close()

# --- Database Functions

def add_action(name):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO actions (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showwarning("Duplicate Action", f"The action '{name}' already exists!")
    finally:
        conn.close()

def get_actions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, count FROM actions")
    actions = cursor.fetchall()
    conn.close()
    return actions

def delete_action(action_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM actions WHERE id = ?", (action_id,))
    conn.commit()
    conn.close()

def add_count(count, action_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE actions SET count = count + ? WHERE id = ?", (count, action_id,))
    conn.commit()
    conn.close()

def add_one_count(action_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE actions SET count = count + 1 WHERE id = ?", (action_id,))
    conn.commit()
    conn.close()    

## --- GUI Functionality
def refresh_actions():
    action_list.delete(0, tk.END)  # clear the listbox
    global action_id_map
    action_id_map = {}
    actions = get_actions()
    for display_idx, action in enumerate(actions, start=1):
        action_id, name, count = action
        action_id_map[display_idx] = action_id

        # Build the line text
        line_text = f"{display_idx}: {name} [{count}]"

        # Insert into listbox
        action_list.insert(tk.END, line_text)

        # Color the line based on count
        if count > 0:
            action_list.itemconfig(tk.END, {'fg':'green'})
        else:
            action_list.itemconfig(tk.END, {'fg':'red'})

def add_action_GUI():
    name = action_entry.get()
    if name.strip():
        add_action(name)
        action_entry.delete(0, tk.END)
        refresh_actions()
    else:
        messagebox.showerror("Error", "Action cannot be empty!!!")

def delete_action_gui():
    selection = action_list.curselection()
    if selection:
        display_idx = selection[0] + 1
        db_id = action_id_map[display_idx]
        delete_action(db_id)
        refresh_actions()
    else:
        messagebox.showerror("Error", "Selection cannot be empty!!!") 


def add_count_gui():
    selection = action_list.curselection()
    count = count_entry.get()
    if selection and count:
        display_idx = selection[0] + 1
        db_id = action_id_map[display_idx]
        add_count(count, db_id)
        refresh_actions()
    else:
        messagebox.showerror("Error", "Selection cannot be empty!!!")

def add_one_count_gui():
    selection = action_list.curselection()
    if selection:
        display_idx = selection[0] + 1
        db_id = action_id_map[display_idx]
        add_one_count(db_id)
        refresh_actions()
    else:
        messagebox.showerror("Error", "Selection cannot be empty!!!")  

## -- GUI Important

root = tk.Tk()
root.title("Action Counter App")
root.geometry("400x650")
root.configure(bg="#0F0F0F")

## - Actual GUI

top_frame = tk.Frame(root, bg="#0F0F0F")
top_frame.pack(fill="x", pady=5)

logo_path = os.path.join(script_directory, "logo.png")
icon_path = os.path.join(script_directory, "my_icon.png")


if os.path.exists(logo_path):
    from PIL import Image, ImageTk, ImageDraw # type: ignore
    original_image = Image.open(logo_path).convert("RGBA")
    resized_image = original_image.resize((50, 50), Image.Resampling.LANCZOS)

    mask = Image.new("L", (50, 50), 0)  # L = greyscale (mask)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 50, 50), fill=255)  # white circle

    if os.path.exists(icon_path):
        original_image2 = Image.open(logo_path).convert("RGBA")
        resized_image2 = original_image.resize((50, 50), Image.Resampling.LANCZOS)
        resized_image2.putalpha(mask)
        icon_img = ImageTk.PhotoImage(resized_image)

        icon_label = tk.Label(root, image=icon_img, bg="#0F0F0F")
        icon_label.pack(side="bottom", anchor="w", padx=10, pady=10)

    resized_image.putalpha(mask)

    logo_img = ImageTk.PhotoImage(resized_image)

    logo_label = tk.Label(top_frame, image=logo_img, bg="#0F0F0F")
    logo_label.pack(side = "right", padx=10, pady=10)


    if os.path.exists(icon_path):
        icon_image = ImageTk.PhotoImage(file=icon_path)
        root.iconphoto(False, icon_image)

title_button = tk.Button(top_frame, text="  Repeatable Action Counter  ", bg="#252525", fg="White",
                            font=("Helvetica", 13, "bold"))
title_button.pack(side = "left", padx=35)

action_entry = tk.Entry(root, width=20, font=("Helvetica", 10))
action_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#0F0F0F")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Action", bg="#252525", fg="white",
                       font=("Helvetica", 10, "bold"), command=add_action_GUI)
add_button.pack(side = "left", padx=5)

delete_button = tk.Button(button_frame, text="Delete Action", bg="#252525", fg="white",
                          font=("Helvetica", 9, "bold"), command=delete_action_gui)
delete_button.pack(side = "left", padx=5)

count_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
count_entry.pack(pady=10)

add_count_button = tk.Button(root, text="   Add Count   ", bg="#252525", fg="white",
                       font=("Helvetica", 10, "bold"), command=add_count_gui)
add_count_button.pack(pady=5)

add_count_button = tk.Button(root, text="Add One to Count", bg="#252525", fg="white",
                       font=("Helvetica", 8, "bold"), command=add_one_count_gui)
add_count_button.pack(pady=5)

action_list = tk.Listbox(root, width=30, height=15, font=("Helvetica", 12), fg="red")
action_list.pack(pady=5)


action_color = "black"

# --- ACTION ID mapping 
action_id_map = {}

refresh_actions()
root.mainloop()