from fastapi import APIRouter
from api import task_endpoints as task_router
router = APIRouter()


router.include_router(
    task_router.router,
    prefix="/tasks",
    tags=["Tasks"],
)
