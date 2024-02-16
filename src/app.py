from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.controllers.RouteController import RouteController
from src.sqlalchemy_db.tables import create_tables, drop_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)
route_controller = RouteController()
app.include_router(route_controller.router)