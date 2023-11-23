from fastapi import FastAPI
import uvicorn
from database import engine
from models.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
from routers import user, telegram_send, task


app.include_router(user.router, prefix="/user")
app.include_router(telegram_send.router, prefix='/telegram')
app.include_router(task.router, prefix='/task')


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
