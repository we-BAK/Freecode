import json
from dataclasses import asdict, dataclass
from typing import List


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task(**task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([asdict(t) for t in self.tasks], f, indent=4)

    def add_task(self, title: str):
        task_id = max([t.id for t in self.tasks], default=0) + 1
        new_task = Task(id=task_id, title=title)
        self.tasks.append(new_task)
        self._save_tasks()
        print(f"Added task: '{title}' (ID: {task_id})")

    def toggle_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                self._save_tasks()
                status = "Done" if task.completed else "Pending"
                print(f"Task {task_id} marked as {status}.")
                return
        print(f"Task ID {task_id} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for t in self.tasks:
            status = "✓" if t.completed else " "
            print(f"[{status}] {t.id}: {t.title}")


# Example usage:
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Learn Python Decorators")
    manager.add_task("Build an API scraper")
    manager.list_tasks()
    manager.toggle_task(1)
    manager.list_tasks()