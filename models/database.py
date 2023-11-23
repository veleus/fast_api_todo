
from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_tasks = Column(String)
    time_task = Column(String)
    end_time = Column(String)


class TaskOld(Base):
    __tablename__ = "task_old"
    id = Column(Integer, primary_key=True, autoincrement=True)
    old = Column(String)


