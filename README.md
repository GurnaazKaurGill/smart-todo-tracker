# Smart To-Do & Time Tracker App
#### Video Demo: https://youtu.be/jWEU0qYh-X4
#### Description:

This is my final project for **CS50’s Introduction to Programming with Python** — a command-line based **Smart To-Do & Time Tracker App** built entirely in Python. It’s a lightweight, yet powerful task management system that lets users add, list, complete, and delete tasks, while also tracking how long each task took to complete from creation to completion.

The app is meant to be practical and simple, designed for people who prefer working in the terminal and want to stay organized without using bulky task management tools. Each task is timestamped and saved to a JSON file, which ensures persistence across sessions.

---

### 🔍 Project Overview:

The program supports the following features:

- **Add Task:** Users can input a title and add a new task. Each task is saved with the current timestamp in IST (Indian Standard Time).
- **List Tasks:** Displays all tasks in a neatly formatted table using the `tabulate` module. Each row shows task number, title, status (✔ or ✘), creation time, completion time (if done), and the total time taken.
- **Mark as Completed:** Marks a specific task as done, logs the time, and calculates how long it took to complete.
- **Delete Task:** Removes a task from the JSON file.
- **Persistent Storage:** Tasks are stored in a file named `tasks.json`, so they are not lost after the program exits.

---

### 📁 Files Included:

- `project.py`: This is the main Python file that contains all the functionality of the app, including the task management functions and the command-line interface. It uses standard libraries like `datetime`, `os`, and `json`, as well as third-party libraries `tabulate` and `pytz`.

- `tasks.json`: This file is automatically created and updated to store all tasks in a structured JSON format. It persists between runs and is used to load and save task data.

- `test_project.py` : This file contains test functions to validate core operations like adding, completing, and deleting tasks using assertions.

- `README.md`: This file, which you're reading now, explains the purpose, structure, and usage of the project.

---

### ⚙️ Design Decisions:

- **Time Tracking:** I chose to include task duration tracking because it's a real-world feature that makes task lists more useful. This required careful handling of timezones, so I used the `pytz` module to ensure accurate time representation in IST.

- **Tabular Output:** For better readability, I used the `tabulate` module instead of printing raw lists or dictionaries. This helped in presenting tasks in a clean, user-friendly format in the terminal.

- **JSON Storage:** I opted for JSON instead of a database to keep the project simple, portable, and beginner-friendly while still ensuring persistent storage.

- **CLI Interface:** The entire app runs in the terminal, which aligns with the goals of CS50P — to build understanding of backend logic without needing complex UI frameworks.

---

### 📈 Possible Improvements:

- Add support for editing task titles
- Include task categories or priorities
- Add filters for showing only completed/incomplete tasks
- Export tasks to CSV or text format
- Build a GUI version using Tkinter or a web version using Flask/Django in future iterations

---

### 🙌 Final Thoughts:

CS50P was an incredible journey — I gained a deep understanding of Python fundamentals and got to apply them in a meaningful way through this project. Building this app helped me practice working with file I/O, timestamps, JSON, external modules, and most importantly, designing a small but functional application from scratch. I look forward to improving this project further and building more complex applications in the future!

