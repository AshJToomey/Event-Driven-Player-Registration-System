# ⚽ Event-Driven Player Registration System

This is a simple Python project demonstrating event-driven programming with a Tkinter graphical interface. It simulates a football environment where registering a player triggers automated actions like notifying teammates and sending messages.



## 🧠 Key Concepts

- **Event-Driven Architecture**:Events like player_registered trigger registered handler functions.
- **GUI Interface**: A user-friendly Tkinter window replaces terminal inputs.
- **Modular Code**: Logic is split across separate files for clarity and reusability.
- **Testing with Pytest**: Core logic is tested using pytest for reliability.

## 📂 File Structure

event_systems_project/

├── main.py          # GUI + main logic to register a player and trigger events

├── functions.py     # Event handler functions (e.g., notify teammates)

├── event_systems.py # Core event registration and dispatch system

├── test_event_systems.py # Pytest tests for event logic

└── README.md        # Project documentation

## 🚀 How to Run

1. Clone the project:

git clone https://github.com/yourusername/event-system-gui.git
cd event-system-gui

2. Run the app:

python main.py

3. A window will open. Enter a player's name and goal count, then click "Register Player".


## 🧪 Testing
We use pytest to ensure the event system works as expected.

Run Tests:

pip install pytest
pytest

## 📌 Example Behavior
After submitting the form:

✅ Player is saved

✅ Two event handlers are triggered:

  - A message is sent

  - Teammates are notified


✅ A success popup appears

Example Output:

Player was saved: Ashley 100

Message sent to: Ashley

Teammates were notified: Ashley

## ✅ Features
- Custom event registration and dispatch system

- Multiple handlers per event

- GUI for user interaction

- Clean, modular structure

- Unit tests with pytest


## 💡 Possible Extensions
- Add event types like goal_scored, injury_reported

- Save players to a file or database

- Display registered players in the GUI

- Replace print with logging

- Add more unit tests

## 📚 License
This project is for educational purposes. Feel free to explore, modify, and build on it!
