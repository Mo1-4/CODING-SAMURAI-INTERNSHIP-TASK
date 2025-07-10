import time
class Task:
    def __init__(self, task_name) -> None:
        if isinstance(task_name, str):
            self.task_name = task_name
        self.done = False
    
    def done_task(self):
        self.done = not self.done

    def conversion(self):
        return f"{self.task_name} [ {"✅" if self.done else "❌"} ] "

class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, name):
        new_task = Task(str(name))
        self.tasks.append(new_task)
        print("=" * 20)
        print(f"{new_task.task_name} Added Successfully")
        print("=" * 20)

    def delete_task(self, index):
        try:
            if self.tasks == []:
                print("=" * 20)
                print("There Is No Task To Delete!")
                print("=" * 20)
        
            elif ((index - 1) != -1):
                self.tasks.pop(index - 1)
                print("=" * 20)
                print(f"Task Number {index} Deleted Successfully")
                print("=" * 20)

        except:
            print("=" * 20)
            print("Bad Input, Try Again!")
            print("=" * 20)


    def toggle_done(self, index):
        try:
            if self.tasks == []:
                print("=" * 20)
                print("There Is No Task To Mark!")
                print("=" * 20)

            elif ((index - 1) != -1):
                self.tasks[index - 1].done_task()
                print("=" * 20)
                print(f"Task '{self.tasks[index-1].task_name}' Marked Successfully")
                print("=" *20)

        except:
            print("=" * 20)
            print("Bad Input, Try Again!")
            print("=" * 20)
                 

    def edit_task(self, index, edit_name):
        try:
            if self.tasks == []:
                print("=" * 20)
                print("There Is No Task To Edit!")
                print("=" * 20)
            
            elif ((index - 1) != -1):
                self.tasks[index - 1].task_name = edit_name
                print("=" * 20)
                print(f"Task Number {index} Edited Successfully")
                print("=" *20)


        except:
            print("=" * 20)
            print("Bad Input, Try Again!")
            print("=" * 20)
                 

    def display_task(self):
        print("=" * 20)
        for task in self.tasks:
            print(f"{self.tasks.index(task) + 1}- {task.conversion()}")
        print("=" * 20)
        


tasks = TaskManager()

print("=" * 51)
print("="*3,"Welcome To-Do List Program Feel Excited To:","="*3)
print("="*18, "See Your Tasks", "="*17)
print("="*20, "Add Tasks", "="*20)
print("="*19, "Delete Tasks", "="*18)
print("="*13, "And Edit Your Task Info", "="*13)
print("=" * 51)

while True:
    try:
        print("1- Add Task")
        print("2- Read Tasks")
        print("3- Delete Task")
        print("4- Mark (Done, Not Done) Task")
        print("5- Edit Task")
        print("6- Quit")
        inp = input("Select Option: ")
        if inp == "1":
            task_inp = input("Enter Your Task: ")
            time.sleep(0.5)
            tasks.add_task(task_inp)

        elif inp == "2":
            time.sleep(0.5)
            tasks.display_task()

        elif inp == "3":
            delete_inp = input("Enter Your Task Number To Delete: ")
            time.sleep(0.5)
            tasks.delete_task(int(delete_inp))

        elif inp == "4":
            mark_inp = input("Enter Your Task Number To mark: ")
            time.sleep(0.5)
            tasks.toggle_done(int(mark_inp))

        elif inp == "5":
            edit_num = input("Enter Your Task Number To Edit: ")
            edit_name = input("Enter Your Edit Name: ")
            time.sleep(0.5)
            tasks.edit_task(int(edit_num), edit_name)

        elif inp == "6":
            print("=" * 20)
            print("Good Bye!")
            print("Exit Program...")
            print("=" * 20)
            time.sleep(1)
            break

        else:
            print("=" * 20)
            print("Bad Option, Try Again!")
            print("=" * 20)
            time.sleep(0.5)

    except:
        print("\n")
        print("=" * 20)
        print("Bad Input, Try Again!")
        print("=" * 20)
        time.sleep(0.5)
