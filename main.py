from fastapi import FastAPI
from contextlib import asynccontextmanager

from routes import tasks

from database import create_table


@asynccontextmanager
async def lifespan(app_: FastAPI):
    await create_table()
    print("База данных успешно подключена!")
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(tasks)