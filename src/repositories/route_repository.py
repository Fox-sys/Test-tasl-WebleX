from typing import List

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.models.point import Point
from src.models.route import RouteAdd, RouteGet
from src.sqlalchemy_db.engine import new_session
from src.sqlalchemy_db.tables import RouteTable
from .point_repository import PointRepository


class RouteRepository:
    @classmethod
    async def add(cls, data: RouteAdd, points: List[Point]):
        async with new_session() as session:
            route_dict = data.model_dump()
            route = RouteTable(**route_dict)
            session.add(route)
            await session.flush()
            await session.commit()
            await PointRepository.bulk_add(points, route)
            await session.flush()
            return route.id

    @classmethod
    async def get_by_id(cls, id: int):
        async with new_session() as session:
            query = select(RouteTable).options(joinedload(RouteTable.points)).where(RouteTable.id == id)
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def all(cls):
        async with new_session() as session:
            query = select(RouteTable)
            result = await session.execute(query)
            return result.scalars().all()
