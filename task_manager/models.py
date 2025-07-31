class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def display(self):
        status = "✓ Done" if self.completed else "⏳ Pending"
        print(f"Task: {self.title} | {status}")
        print(f"Description: {self.description}")

class DeadlineTask(Task):
    def __init__(self, title, description, due_date):
        super().__init__(title, description)
        self.due_date = due_date

    def display(self):
        super().display()
        print(f"Due Date: {self.due_date}")
