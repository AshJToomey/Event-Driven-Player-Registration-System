#program 1 - main
import tkinter as tk
from tkinter import messagebox

from event_systems import register_event, dispatch
from functions import notify_teammates, send_message

# Backend logic
def create_player(name: str, goals: int):
    print("Player was saved:", name, goals)
    dispatch('player_registered', name)
    messagebox.showinfo("Success", f"Player '{name}' registered with {goals} goals.")

# Register event handlers
register_event('player_registered', send_message)
register_event('player_registered', notify_teammates)

# GUI Setup
def submit():
    name = name_entry.get().strip()
    goals_str = goals_entry.get().strip()

    if not name or not goals_str:
        messagebox.showerror("Error", "Please enter both name and goals.")
        return

    try:
        goals = int(goals_str)
    except ValueError:
        messagebox.showerror("Error", "Goals must be a number.")
        return

    create_player(name, goals)

# Initialize Tkinter
root = tk.Tk()
root.title("Player Registration")
root.geometry("300x200")
root.resizable(False, False)

# GUI Elements
tk.Label(root, text="Player Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Goals Scored:").pack(pady=(10, 0))
goals_entry = tk.Entry(root, width=30)
goals_entry.pack()

tk.Button(root, text="Register Player", command=submit).pack(pady=20)

root.mainloop()
