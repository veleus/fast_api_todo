from fastapi import APIRouter
from database import db
from sender_tg.send_tg import SendTask

router = APIRouter()

@router.get('/get_old_task', tags=['telegram'])
async def get_ync(id:int):
    return SendTask.get_task(db,id)