from typing import List

from src.models.point import Point
from src.sqlalchemy_db.engine import new_session
from src.sqlalchemy_db.tables import RouteTable, PointTable


class PointRepository:
    @classmethod
    async def bulk_add(cls, points: List[Point], route: RouteTable):
        async with new_session() as session:
            objects = [PointTable(**i.model_dump(), route_id=route.id) for i in points]
            session.add_all(objects)
            await session.commit()
