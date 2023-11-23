from sqlalchemy.orm import Session
from models.database import Task
from dto import task as NewTask



def get_task(db: Session, user_id:str):
    return db.query(Task).filter(Task.id == user_id).first()

def create_tas(db: Session, task: NewTask.TaskModel):
    exp = Task(name_tasks=task.user_name, time_task=task.time,  end_time=task.end_time )
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp


def update_task(db: Session,id: int, user: NewTask.TaskModel):
    existing_user = db.query(Task).filter(Task.id == id).first()
    existing_user.name_tasks = user.user_name
    existing_user.time_task = user.time
    existing_user.end_time = user.end_time
    db.commit()
    db.refresh(existing_user)
    return existing_user


def delete_tasks(db: Session, id: int):
    return db.query(Task).filter(Task.id == id).delete()

