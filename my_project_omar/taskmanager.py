from typing import Dict, Optional
from modules import  UrgentTask, CreateTaskBase,UpdateDetails
from uuid import UUID, uuid4
from Tasks import Task

tasks_dict = {}
class TaskManager:
    
    def create_task(self, task_data: CreateTaskBase) -> Task :
        title=task_data.title
        description=task_data.description
        due_date=task_data.due_date
        status=task_data.status
          
        if task_data.priority:
            add_urgent=UrgentTask(task_data.priority,title,description,due_date,status)
            tasks_dict[add_urgent.task_id]=add_urgent
        else:
            add_task=Task(title,description,due_date,status)
            tasks_dict[add_task.task_id]=add_task
        
    def get_tasksbyid(self, task_id: str) -> Optional[Task]:
      return self.tasks_dict.get(task_id)
    
    def get_tasks(self)-> Dict[str, Task]:
      return self.tasks_dict
#   Default value
    def update_task(self, task_id: str, update_data: UpdateDetails) -> Optional[Task]:
      if task_id in tasks_dict:
         task = tasks_dict[task_id]
         task.update_details(update_data)
         return task
      return None
    
    def delete_task(self, task_id: str) -> Optional[Task]:
        return self.tasks_dict.pop(task_id)     