import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# File paths for storing tasks, notes, and highlighted task indices
TASKS_FILE = "tasks.txt"
NOTES_FILE = "notes.txt"
HIGHLIGHTS_FILE = "highlights.txt"

# Reads all lines from a file and returns them as a list of strings
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Writes a list of strings to a file, each item on a new line
def write_file(filename, data):
    with open(filename, "w") as file:
        file.write("\n".join(data) + "\n")

# Refreshes the task listbox with current tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in read_file(TASKS_FILE):
        task_listbox.insert(tk.END, task)
    apply_highlights()  # Apply highlights after loading tasks

# Refreshes the note listbox with current notes
def update_note_listbox():
    note_listbox.delete(0, tk.END)
    for note in read_file(NOTES_FILE):
        note_listbox.insert(tk.END, note)

# Adds a new task to the task list
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks = read_file(TASKS_FILE)
        tasks.append(task)
        write_file(TASKS_FILE, tasks)
        task_entry.delete(0, tk.END)
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Deletes the currently selected task
def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        return
    tasks = read_file(TASKS_FILE)
    del tasks[selected_index[0]]
    write_file(TASKS_FILE, tasks)
    update_task_listbox()

# Adds a new note with timestamp to the note list
def add_note():
    note = note_entry.get().strip()
    if note:
        notes = read_file(NOTES_FILE)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        notes.append(f"{note}    -    {timestamp}")
        write_file(NOTES_FILE, notes)
        note_entry.delete(0, tk.END)
        update_note_listbox()
    else:
        messagebox.showwarning("Warning", "Note cannot be empty!")

# Deletes the currently selected note
def delete_note():
    selected_index = note_listbox.curselection()
    if not selected_index:
        return
    notes = read_file(NOTES_FILE)
    del notes[selected_index[0]]
    write_file(NOTES_FILE, notes)
    update_note_listbox()

# Toggles the highlight state of the selected task (highlight/unhighlight)
def toggle_highlight():
    selected_index = task_listbox.curselection()
    if not selected_index:
        return
    index = selected_index[0]
    current_bg = task_listbox.itemcget(index, "bg")
    if current_bg == "yellow":
        task_listbox.itemconfig(index, bg="#FFFACD")  # Default background
        remove_highlight(index)
    else:
        task_listbox.itemconfig(index, bg="yellow")
        save_highlight(index)

# Saves the index of a highlighted task to the highlight file
def save_highlight(index):
    highlights = read_file(HIGHLIGHTS_FILE)
    if str(index) not in highlights:
        highlights.append(str(index))
        write_file(HIGHLIGHTS_FILE, highlights)

# Removes the index of a highlighted task from the highlight file
def remove_highlight(index):
    highlights = read_file(HIGHLIGHTS_FILE)
    if str(index) in highlights:
        highlights.remove(str(index))
        write_file(HIGHLIGHTS_FILE, highlights)

# Applies highlights to the tasks listbox based on stored indices
def apply_highlights():
    highlights = read_file(HIGHLIGHTS_FILE)
    for index in highlights:
        task_listbox.itemconfig(int(index), bg="yellow")

# === GUI Setup ===
root = tk.Tk()
root.title("Sigma Manager")
root.geometry("500x500")
root.configure(bg="#87CEEB")  # Light sky blue background

FONT = ("Cooper Black", 10)

# === Task Section ===
task_frame = tk.LabelFrame(root, text="Tasks", font=FONT, bg="#87CEEB")
task_frame.pack(pady=10, padx=10, fill="both", expand=True)

task_entry = tk.Entry(task_frame, width=40, font=FONT)
task_entry.pack(pady=5)

task_button_frame = tk.Frame(task_frame, bg="#87CEEB")
task_button_frame.pack()

add_task_button = tk.Button(task_button_frame, text="Add Task", font=FONT, command=add_task)
add_task_button.pack(side="left", padx=5)

delete_task_button = tk.Button(task_button_frame, text="Delete Task", font=FONT, command=delete_task)
delete_task_button.pack(side="left", padx=5)

highlight_task_button = tk.Button(task_button_frame, text="Highlight Task", font=FONT, command=toggle_highlight)
highlight_task_button.pack(side="left", padx=5)

task_listbox = tk.Listbox(task_frame, width=50, height=7, font=FONT, bg="#FFFACD")
task_listbox.pack(pady=5)

# === Note Section ===
note_frame = tk.LabelFrame(root, text="Notes", font=FONT, bg="#87CEEB")
note_frame.pack(pady=10, padx=10, fill="both", expand=True)

note_entry = tk.Entry(note_frame, width=40, font=FONT)
note_entry.pack(pady=5)

note_button_frame = tk.Frame(note_frame, bg="#87CEEB")
note_button_frame.pack()

add_note_button = tk.Button(note_button_frame, text="Add Note", font=FONT, command=add_note)
add_note_button.pack(side="left", padx=5)

delete_note_button = tk.Button(note_button_frame, text="Delete Note", font=FONT, command=delete_note)
delete_note_button.pack(side="left", padx=5)

note_listbox = tk.Listbox(note_frame, width=50, height=7, font=FONT, bg="#FFFACD")
note_listbox.pack(pady=5)

# Load saved data on startup
update_task_listbox()
update_note_listbox()

# Run the application
root.mainloop()
