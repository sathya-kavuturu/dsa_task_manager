from models import Task
from hash_table import HashTable
from stack import Stack
from action import Action
from queue import Queue

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_map = HashTable()
        self.undo_stack = Stack()
        self.execution_queue = Queue()


    # def add_task(self, task):
    #     steps = 0
    #     for i in self.tasks:
    #         steps += 1
    #         if task == self.tasks:
    #             print("Duplicate task ID")
    #             print(f"it took {steps} steps to find this")
    #             return
    #     self.tasks.append(task)
    #     print("Task added")
    def add_task(self, task):
        if self.task_map.get(task.task_id) is not None:
            print("Duplicate ID")
            return
        self.tasks.append(task)
        self.task_map.put(task.task_id, task)
        self.execution_queue.enqueue(task)


    def list_tasks(self):
        for task in self.tasks:
            print(task)


    # def find_task_by_id(self, task_id):
    #     steps = 0
    #     for task in self.tasks:
    #         steps += 1
    #         if task.task_id == task_id:
    #             print(f"found in {steps} steps")
    #             return task
    #     print(f"Not found after  {steps} steps")
    #     return None
    def find_task_by_id(self, task_id):
        task = self.task_map.get(task_id)

        if task:
            print("found task in O(1)")
        else:
            print("Not Found")
        return task


    # def delete_task(self, task_id):
    #     steps = 0
    #     for i in range(len(self.tasks)):
    #         steps += 1
    #         if self.tasks[i].task_id == task_id:
    #             del self.tasks[i]
    #             print(f"deleted task {task_id} in {steps} steps")
    #             return True
    #     print(f"Not found after  {steps} steps")
    #     return False
    def delete_task(self, task_id):
        task = self.task_map.get(task_id)

        if not task:
            print("Not Found")
            return False
        
        action = Action("DELETE", task)
        self.undo_stack.push(action)
        self.task_map.delete(task_id)

        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                del self.tasks[i]
                break
        print("Deleted Task")
        return True
    

    def undo(self):
        if self.undo_stack.is_empty():
            print("nothing to undo")
            return
        
        action = self.undo_stack.pop()

        if action.action_type == "DELETE":
            task = action.data
            self.tasks.append(task)
            self.task_map.put(task.task_id, task)
            print(f"Undo delete: restored task {task.task_id}")

        elif action.action_type == "STATUS_UPDATE":
            task_id, old_status = action.data
            task = self.task_map.get(task_id)
            if task:
                task.status = old_status
                print(f"Undo status update: task {task_id} restored to {old_status}")


    
    def update_status(self, task_id, new_status):
        task = self.task_map.get(task_id)
        if task is None:
            print("Task not found")
            return

        action = Action("STATUS_UPDATE", (task_id, task.status))
        self.undo_stack.push(action)

        task.status = new_status
        print(f"Task {task_id} status updated to {new_status}")
        return True
    

    def execute_next_task(self):
        task = self.execution_queue.dequeue()
        if not task:
            print("NO tasks to execute")
            return 
        print(f"Executing task {task.task_id}: {task.title}")
        task.status = "DONE"
        




