from pathlib import Path

tasks_file = Path("tasks.txt")
tasks = []


def load_tasks():
    if tasks_file.exists():
        with tasks_file.open("r", encoding="utf-8") as file:
            tasks = file.readlines()

        tasks = [task.strip() for task in tasks]
        return tasks
    else:
        return []


def save_tasks(tasks):
    with tasks_file.open("w", encoding="utf-8") as file:
        for item in tasks:
            file.write(item + "\n")


def sort_list(tasks):
    tasks.sort(key=lambda x: x.split()[-1])
    return [f"{i}-{task.split('-',1)[-1]}" for i, task in enumerate(tasks, 1)]


while True:
    print("\n1- Show list")
    print("2- Add")
    print("3- Delete")
    print("0- Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        tasks = load_tasks()

        if len(tasks) == 0:
            print("List is empty")
        else:
            for task in tasks:
                print(task)

    elif choice == 2:
        tasks = load_tasks()

        print("Help: work 07:45 | enter 0 to exit")
        while True:
            task = input("Enter task: ")

            if task == "0":
                break

            tasks.append(task)
            tasks = sort_list(tasks)

        save_tasks(tasks)

    elif choice == 3:
        tasks = load_tasks()

        if len(tasks) == 0:
            print("List is empty")
            continue

        for task in tasks:
            print(task)

        try:
            remove = int(input("Enter task number: "))

            if 1 <= remove <= len(tasks):
                tasks.pop(remove - 1)
                tasks = sort_list(tasks)
                save_tasks(tasks)
                print("Task deleted")
            else:
                print("Invalid task number")

        except ValueError:
            print("Please enter a number")

    elif choice == 0:
        break
