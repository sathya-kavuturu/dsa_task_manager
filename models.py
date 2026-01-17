class Task:
    def __init__(self,task_id, title, priority, due_date, status="PENDING"):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status
    
    
    def __repr__(self):
        return f"{self.task_id} | {self.title} | {self.priority} | {self.due_date} | {self.status}"