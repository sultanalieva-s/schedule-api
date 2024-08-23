from typing import List

from bson import ObjectId

from exceptions.common_exceptions import NotFoundException
from schemas.task import Task


class TaskRepository:
    def __init__(self, db):
        self._db = db

    async def create(self, task: Task) -> Task:
        collection = self._db["tasks"]
        created_task_id = collection.insert_one(task.model_dump()).inserted_id
        print(f"a task has been inserted: {created_task_id}")
        task = collection.find_one(filter=created_task_id)
        task["_id"] = str(task["_id"])
        return task

    async def delete(self, task_id: str) -> None:
        collection = self._db["tasks"]
        task_id = ObjectId(task_id)
        collection.find_one_and_delete({"_id": task_id})

    async def get(self) -> List[Task]:
        collection = self._db["tasks"]
        tasks = list(collection.find())
        for task in tasks:
            task["_id"] = str(task["_id"])
        return tasks

    async def get_by_id(self, task_id: str) -> Task:
        collection = self._db["tasks"]
        task_id = ObjectId(task_id)
        task = collection.find_one({"_id": task_id})
        if task is None:
            raise NotFoundException(f"Task with id {task_id} was not found")
        task["_id"] = str(task["_id"])
        return task

    async def update(self, task_id, task_data):
        collection = self._db["tasks"]
        task_id = ObjectId(task_id)
        collection.update_one({"_id": task_id}, {"$set": task_data.dict()})
        updated_task = collection.find_one({"_id": task_id})
        updated_task["_id"] = str(updated_task["_id"])
        return updated_task
