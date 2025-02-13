from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskID

tasks = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@tasks.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@tasks.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return tasks


@tasks.delete("/<int:task_id>")
async def delete_task(task_id: int):
    await TaskRepository.delete_one(task_id)
    return {"ok": True}


