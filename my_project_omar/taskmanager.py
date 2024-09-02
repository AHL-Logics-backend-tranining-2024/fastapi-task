from typing import Dict, Optional
from modules import Task, UrgentTask, TaskCreate
from uuid import UUID, uuid4

tasks_dict = {}
class TaskManager:
    def create_task(self, task_data: TaskCreate) -> Task:

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
    def update_task(self, task_id: str, task_data: TaskCreate) -> Optional[Task]:
      if task_id in self.tasks_dict:
           
            if task_data.priority:
                updated_task = UrgentTask(
# uuid give me a unique id for each task 
                title=task_data.title,
                description=task_data.description,
                due_date=task_data.due_date,
                status=task_data.status,
                priority=self.urgent_tasks_db[task_id].priority ) # Keep the current priority)
                self.tasks_dict[task_id]=updated_task
            else:
                updated_task = Task(
                title=task_data.title,
                description=task_data.description,
                due_date=task_data.due_date,
                status=task_data.status)
                self.tasks_dict[task_id]=updated_task

    def delete_task(self, task_id: str) -> Optional[Task]:
        return self.tasks_dict.pop(task_id)

       
                
                
                
                