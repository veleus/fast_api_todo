from sqlalchemy.orm import Session
from models.database import Task
from dto import task as NewTask
from database import engine, db
import requests
from config import Telegram


class SendTask():

    def get_task(db: Session, user_id:int):

       
        time_task = db.query(Task.end_time, Task.time_task, Task.name_tasks).filter(Task.id == user_id).first()
       
        url_req = "https://api.telegram.org/bot" + Telegram.TELEGRAM_BOT + "/sendMessage" + "?chat_id=" + Telegram.CHAT_ID + "&text=" + f"Ваша задача под номером: {user_id}:\nEndTime: {time_task.end_time}\nStartTime: {time_task.time_task}\nDescription:{time_task.name_tasks}"
        
        return requests.get(url_req).json()
        
        
        
    

    
    

