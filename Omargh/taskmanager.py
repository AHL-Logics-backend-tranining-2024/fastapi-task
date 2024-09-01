from typing import Dict, Optional
from modules import Task, UrgentTask, TaskCreate
from uuid import UUID, uuid4

tasks_dict = {}
class TaskManager:
    def create_task(self, task_data: TaskCreate, is_urgent: bool = False) -> Task:
# uuid give me a unique id for each task 
        new_task_id = str(uuid4())
        task_id=UUID(new_task_id),
        title=task_data.title,
        description=task_data.description,
        due_date=task_data.due_date,
        status=task_data.status,
        priority="High"  # Default priority for urgent tasks   
        if is_urgent:
            add_urgent=UrgentTask(priority,title,description,due_date,status)
            tasks_dict[add_urgent.task_id]=add_urgent
        else:
            add_task=Task(title,description,due_date,status)
            tasks_dict[add_task.task_id]=add_task
        
    def view_tasksbyid(self, task_id: str) -> Optional[Task]:
      return self.tasks_dict.get(task_id)
    def view_tasks(self)-> Dict[str, Task]:
      return self.tasks_dict
#   Default value
    def update_task(self, task_id: str, task_data: TaskCreate,is_urgent: bool = False) -> Optional[Task]:
      if task_id in self.tasks_dict:
           
            if is_urgent:
                updated_task = UrgentTask(
# uuid give me a unique id for each task 
                task_id=UUID(task_id),
                title=task_data.title,
                description=task_data.description,
                due_date=task_data.due_date,
                status=task_data.status,
                priority=self.urgent_tasks_db[task_id].priority ) # Keep the current priority)
                self.tasks_dict[task_id]=updated_task
            else:
                updated_task = Task(
                task_id=UUID(task_id),
                title=task_data.title,
                description=task_data.description,
                due_date=task_data.due_date,
                status=task_data.status)
                self.tasks_dict[task_id]=updated_task

    def delete_task(self, task_id: str) -> Optional[Task]:
        return self.tasks_dict.pop(task_id)

       
                
                
                
                