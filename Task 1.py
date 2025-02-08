class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completion_status = []

    def add_task(self, task):
        self.tasks.append(task)
        self.completion_status.append(False)

    def mark_completed(self, task):
        if task in self.tasks:
            index = self.tasks.index(task)
            self.completion_status[index] = True
        else:
            print(f"Task '{task}' not found.")

    def view_completed_tasks(self):
        print("Completed Tasks:")
        for i, task in enumerate(self.tasks):
            if self.completion_status[i]:
                print(f"{i+1}. {task}")

to_do = ToDoList()
to_do.add_task("Buy groceries")
to_do.add_task("Complete homework")
to_do.mark_completed("Buy groceries")
to_do.view_completed_tasks()