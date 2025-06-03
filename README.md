# ⚽ Event-Driven Player Registration System

This is a simple Python project demonstrating **event-driven programming** with a **Tkinter-based graphical interface**. It simulates a football environment where registering a player triggers automated actions such as notifying teammates and sending a message.



## 🧠 Key Concepts

- **Event-Driven Architecture**:Events like player_registered trigger registered handler functions.
- **GUI Interface**: A user-friendly Tkinter window replaces terminal inputs.
- **Modular Code**: Logic is split across main.py, functions.py, and event_systems.py for clarity and reusability.

## 📂 File Structure

event_systems_project/
├── main.py # GUI + main logic to register a player and trigger events
├── functions.py # Event handler functions (e.g., notify teammates)
├── event_systems.py # Core event registration and dispatch system
└── README.md # Project documentation

## 🚀 How to Run

1. Clone or download the project:

git clone https://github.com/yourusername/event-system-gui.git
cd event-system-gui

2. Make sure you have Python 3 installed.

3. Run the app:

python main.py

4. A window will open. Enter a player's name and goal count, then click "Register Player".

## 🧪 Example Behavior
After submitting the form:

- The player is saved (output printed to the terminal).

- Two events fire:

   - A message is sent.

   - Teammates are notified.

- A success popup confirms registration.

Example Output:
Player was saved: Ashley 100
Message sent to: Ashley
Teammates were notified: Ashley

## ✅ Features
Custom event registration and dispatch system

Multiple handlers per event

GUI for user interaction

Clean, modular structure

## 💡 Possible Extensions
Add event types like goal_scored, injury_reported

Save players to a file or database

Display a list of registered players in the GUI

Use logging instead of print statements

Add automated tests with unittest or pytest


## 📚 License
This project is for educational purposes. Feel free to explore, modify, and build on it!
