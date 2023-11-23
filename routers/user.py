from fastapi import APIRouter
from database import db
from dto import users as User_new
from operations import crud

router = APIRouter()


@router.get("/get_user/{id}", tags=["user"])
async def root(id: int):
    user = crud.get_db(db, id)
    return user
    
@router.post("/create_user", tags=['user'])    
async def create_user(user: User_new.ItemBase):
    return crud.create_user(db, user)

@router.put("/update_user", tags=['user'])
async def update_user(id: int, user: User_new.ItemBase):
    return crud.update_user(db, id, user)

@router.delete("/del_user/{id}", tags=['user'])
async def delete_user(id: int):
    return crud.delete_user(db, id)
