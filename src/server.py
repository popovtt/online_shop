from contextlib import asynccontextmanager

import uvicorn

from src.service import AppService
from src.utils.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: AppService):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

app = AppService(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("src.server:app")