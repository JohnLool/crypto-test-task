from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import router
from app.core.database import create_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)
