from exceptions.common_exceptions import NotFoundException
from resource_access.repositories.task_repository import TaskRepository
from schemas.task import Task


async def create_task_usecase(db, task_data: Task):
    task_repo = TaskRepository(db)
    return await task_repo.create(task_data)


async def update_task_usecase(db, task_id: str, task_data: Task):
    task_repo = TaskRepository(db)
    task = await task_repo.get_by_id(task_id)
    if task is None:
        raise NotFoundException(f"Task with id {task_id} was not found")
    return await task_repo.update(task_id, task_data)


async def get_tasks_usecase(db):
    task_repo = TaskRepository(db)
    return await task_repo.get()


async def get_task_by_id_usecase(db, task_id):
    task_repo = TaskRepository(db)
    return await task_repo.get_by_id(task_id)


async def delete_task_usecase(db, task_id: str):
    task_repo = TaskRepository(db)
    return await task_repo.delete(task_id)

