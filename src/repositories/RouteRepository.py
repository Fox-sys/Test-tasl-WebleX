from sqlalchemy import select

from src.models.Route import RouteAdd
from src.sqlalchemy_db.engine import new_session
from src.sqlalchemy_db.tables import RouteTable


class RouteRepository:
    @classmethod
    async def add(cls, data: RouteAdd) -> int:
        async with new_session() as session:
            route_dict = data.model_dump()
            route = RouteTable(**route_dict)
            session.add(route)
            await session.flush()
            await session.commit()
            return route.id

    @classmethod
    async def get_by_id(cls, id: int):
        async with new_session() as session:
            query = select(RouteTable).where(id=id)
            result = await session.execute(query)
            return result.one_or_none()

    @classmethod
    async def all(cls):
        async with new_session() as session:
            query = select(RouteTable)
            result = await session.execute(query)
            return result.scalars().all()
