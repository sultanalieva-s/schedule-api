from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse, Response

from api.depends import get_db
from exceptions.common_exceptions import NotFoundException
from schemas.task import Task, TaskIn
from usecases.task_usecases import (
    create_task_usecase,
    get_tasks_usecase,
    delete_task_usecase,
    update_task_usecase,
    get_task_by_id_usecase
)

router = APIRouter()


@router.post(
    "/",
    description="Create a task",
    response_model=Task
)
async def create_task(
        task_in: TaskIn,
        db=Depends(get_db),
):
    try:
        return await create_task_usecase(db, task_in)
    except NotFoundException as error:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": error,
                "error_code": error,
            },
        )


@router.put(
    "/{task_id}/",
    description="Update Task",
    response_model=Task
)
async def update_task(
        task_id: str,
        task_in: TaskIn,
        db=Depends(get_db),
):
    try:
        return await update_task_usecase(db, task_id, task_in)
    except NotFoundException as error:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": error.message,
                "error_code": error.error_code,
            },
        )


@router.get(
    "/",
    description="Get All Tasks",
    response_model=List[Task]
)
async def get_tasks(
        db=Depends(get_db),
):
    return await get_tasks_usecase(db)


@router.get(
    "/{task_id}/",
    description="Get Task",
    response_model=Task
)
async def get_task(
        task_id: str,
        db=Depends(get_db),
):
    try:
        await get_task_by_id_usecase(db, task_id)
    except NotFoundException as error:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": error.message,
                "error_code": error.error_code,
            },
        )


@router.delete(
    "/{task_id}/",
    description="Delete Task",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_task(
        task_id: str,
        db=Depends(get_db),
):
    try:
        await delete_task_usecase(db, task_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except NotFoundException as error:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": error.message,
                "error_code": error.error_code,
            },
        )
