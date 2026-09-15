
# ToDo Manager

A simple command-line ToDo Manager written in Python for managing daily tasks.

## Features

- Add new tasks
- Show all tasks
- Delete tasks by number
- Automatic sorting by time
- Save data in `tasks.txt`

## Clone Repository

```bash
git clone https://github.com/patriot1234/Todo_manager.git
cd Todo_manager
```

## Run

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run the program:

```bash
python ToDo_Manager.py
```

---

## Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```
---

## Main Menu

After running the program:

```text
1 - Show list
2 - Add
3 - Delete
0 - Exit
```

---

## Show Tasks

Choose option `1` to display all saved tasks.

Example:

```text
1-work 07:45
2-study 09:30
3-gym 18:00
```

---

## Add Tasks

Choose option `2`.

Enter each task in the following format:

```text
task_name HH:MM
```

Example:

```text
work 07:45
study 09:30
gym 18:00
```

Enter `0` to return to the main menu.

Tasks are automatically sorted by time.

---

## Delete Tasks

Choose option `3`.

The program first displays the task list:

```text
1-work 07:45
2-study 09:30
3-gym 18:00
```

Enter the task number to delete:

```text
Enter task number: 2
```

Output:

```text
Task deleted
```

The remaining tasks are automatically renumbered.

---

## Project Structure

```text
Todo_manager/
├── ToDo_Manager.py
├── tasks.txt
└── README.md
```

---

## Author

**Ali Mazaheri**