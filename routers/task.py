from fastapi import APIRouter
from database import db
from dto import task as NewTask
from operations import create_task

router = APIRouter()


@router.get("/get_task", tags=['task'])
async def get_task(task_id: int):
    task_id = create_task.get_task(db, task_id)
    return task_id


@router.post("/create_task", tags=['task'])
async def create(task: NewTask.TaskModel):
    return create_task.create_tas(db, task)


@router.put("/update_task", tags=['task'])
async def update(id: int , user: NewTask.TaskModel):
    return create_task.update_task(db, id, user)

@router.delete("/delete_task", tags=['task'])
async def delete(id: int):
    return create_task.delete_tasks(db, id)

