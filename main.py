from task_manager.models import Task, DeadlineTask
from task_manager.manager import TaskManager

def main():
    manager = TaskManager()
    manager.add_task(Task("Buy milk", "Go to the store"))
    manager.add_task(DeadlineTask("Submit assignment", "Finish homework", "2025-08-10"))
    manager.complete_task(0)
    manager.show_tasks()

if __name__ == "__main__":
    main()
