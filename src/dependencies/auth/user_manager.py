from fastapi import Depends, BackgroundTasks

from src.auth.user_manager import UserManager
from src.dependencies.auth.users import get_user_db


async def get_user_manager(
    background_tasks: BackgroundTasks,
    user_db=Depends(get_user_db),
):
    yield UserManager(user_db, background_tasks)
