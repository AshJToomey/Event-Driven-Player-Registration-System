# ⚽ Event-Driven Player Registration System

This is a simple Python project demonstrating **event-driven architecture** using custom event registration and dispatching. It models a football environment where a player is registered, triggering notifications to teammates and sending a message automatically.

## 🧠 Key Concepts

- **Event-Driven Programming**: Code responds to events (e.g., `player_registered`) by executing associated handler functions.
- **Modular Code Structure**: Logic is organized into multiple files (`main.py`, `functions.py`, `event_systems.py`) for clarity and scalability.

## 📂 File Structure

event_systems_project/
├── main.py # Core logic to register a player and dispatch events
├── functions.py # Functions triggered by events (e.g., notify, send message)
├── event_systems.py # Custom event system to register and handle events
└── README.md # Project overview and instructions


## 🚀 How to Run

1. Clone the repo or download the files.
2. Ensure Python 3 is installed.
3. Run the main script:
   ```bash
   python main.py

You should see output showing the player being saved and both event handlers responding.

🛠 Example Output
Player was saved Ashley 100
message sent Ashley
Teammates were notified Ashley

✅ Features
Custom event registration system

Event dispatching with multiple handlers

Modular and extendable structure

💡 Possible Extensions
Add more event types like goal_scored or injury_reported

Store players in a database or file

Use logging instead of print statements

Add test cases using unittest or pytest

📚 License
This project is for educational use. Feel free to adapt or extend it!
