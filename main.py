from task_manager import TaskManager
from models import Task


tm = TaskManager()

# tm.add_task(Task(1, "Learn Python", 3, "2026-01-20"))
# tm.add_task(Task(2, "Learn DSA", 5, "2026-02-01"))
# tm.add_task(Task(3, "Build Project", 4, "2026-02-10"))

# tm.list_tasks()

# tm.find_task_by_id(2)
# tm.find_task_by_id(99)

# tm.delete_task(3)

for i in range(1,1001):
    task = Task(
        task_id=i,
        title=f"Task {i}",
        priority=(i%5) +1,
        due_date=f"2026-02-{(i % 28) + 1:02d}"
    )
    tm.add_task(task)
print("\n--- Listing Tasks ---")

tm.list_tasks()

print("\n--- Searching Tasks ---")
print(tm.find_task_by_id(500))   # Average case
print(tm.find_task_by_id(1))  # Best case
print(tm.find_task_by_id(1000))   # Worst case
print(tm.find_task_by_id(9999))   # Not found

print("\n--- Deleting Tasks ---")
tm.delete_task(1)
tm.delete_task(500)
tm.delete_task(1000)
tm.delete_task(9999)

tm.undo()
