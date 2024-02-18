from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, relationship
from src.sqlalchemy_db.engine import engine


class Table(DeclarativeBase):
    pass


class RouteTable(Table):
    __tablename__ = 'routes'

    id: Mapped[int] = MappedColumn(primary_key=True)
    points: Mapped[List["PointTable"]] = relationship(back_populates='route')


class PointTable(Table):
    __tablename__ = 'points'

    id: Mapped[int] = MappedColumn(primary_key=True)
    lat: Mapped[float]
    lng: Mapped[float]
    route: Mapped["RouteTable"] = relationship(back_populates='points')


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Table.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Table.metadata.drop_all)