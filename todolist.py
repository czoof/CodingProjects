import sys

tasks = set()
completed = set()

def display_tasks(task_set):
    return ', '.join(task_set) if task_set else 'None'
def main():

    while True:
        print("1: Add task ")
        print("2: Remove task ")
        print("3: Current tasks ")
        print("4: Completed tasks ")
        print("5: Quit")

        x = input("Enter an option (1/2/3/4/5): ").strip()

        if x == '1':
            add_task()
        elif x == '2':
            remove_tasks()
        elif x == '3':
            current_tasks()
        elif x == '4':
            completed_tasks()
        elif x == '5':
            sys.exit()
        else:
            print("Invalid option, please try again.")


def add_task():
    while True:
        a = input("Enter a task or 'b' to back ")
        if a == 'b':
            main()
        else:
            tasks.add(a)
            print(f"Current tasks: {display_tasks(tasks)}")
            while True:
                b = input("Add another task? type 'yes' or 'b' to go back ")
                try:
                    if b == 'b'.lower():
                        main()
                    elif b == 'yes'.lower():
                        break
                except ValueError:
                    print("Invalid input")
                    continue


def current_tasks():
    while True:
        print(f"Your active tasks: {display_tasks(tasks)}")
        c = input("'1' Mark a task as complete or 'b' to go back ")
        while True:
            if c == '1':
                d = input(str(f"Which task do you want to mark as complete? {display_tasks(tasks)} "))
                if d in tasks:
                    tasks.remove(d)
                    completed.add(d)
                    print(f"Task '{d}' has been marked as complete ")
                    while True:
                        e = input("Mark another task as complete? type 'yes' or 'b' to go back ")
                        try:
                            if e == 'b'.lower():
                                current_tasks()
                            elif e == 'yes'.lower():
                                break
                        except ValueError:
                            continue

            elif c == 'b':
                main()
            else:
                print("Invalid Input")
                break


def completed_tasks():
    while True:
        print(f"Completed tasks: {display_tasks(completed)}")
        f = input("Press 'b' to go back ")
        if f == 'b':
            main()
        else:
            print("Invalid Input")
            continue


def remove_tasks():
    while True:
        print(f"Your current tasks: {display_tasks(tasks)}")
        print(f"Your completed tasks: {display_tasks(completed)}")
        g = input("Press '1' to delete a current task, and '2' to delete a completed task, or 'b' to go back ")
        if g == '1':
            while True:
                h = input(f"Type the current task you want to delete or 'b' to back {display_tasks(tasks)} ")
                if h == 'b':
                    remove_tasks()
                elif h in tasks:
                    tasks.remove(h)
                    print(f"You deleted task '{h}', your current tasks are {display_tasks(tasks)}")
                    while True:
                        i = input("Do you want to delete another task? type 'yes' or 'b' to go back ")
                        try:
                            if i == 'b'.lower():
                                remove_tasks()
                            elif i == 'yes'.lower():
                                break
                        except ValueError:
                            print("Invalid Input")
                            continue

                elif h not in tasks:
                    print("This is not in the tasks")
                    continue

        if g == '2':
            while True:
                j = input(f"Type the completed task you want to delete or 'b' to back {display_tasks(completed)} ")
                if j == 'b':
                    remove_tasks()
                elif j in completed:
                    completed.remove(j)
                    print(f"You deleted task '{j}', your current completed tasks are {display_tasks(completed)}")
                    while True:
                        k = input("Do you want to delete another task? type 'yes' or 'b' to go back ")
                        try:
                            if k == 'b'.lower():
                                remove_tasks()
                            elif k == 'yes'.lower():
                                break
                        except ValueError:
                            print("Invalid Input")
                            continue

                elif j not in tasks:
                    print("This is not in the tasks")
                    continue

        if g == 'b':
            print("Type a task")
            main()

        else:
            print("Invalid Input")
            continue


main()























