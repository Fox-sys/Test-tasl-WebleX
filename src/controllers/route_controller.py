from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.Route import RouteAdd
from src.repositories.route_repository import RouteRepository


class RouteController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route('/api/routes/ping/', self.ping, methods=['GET'])
        self.router.add_api_route("/api/routes/{id}/", self.get_route, methods=['GET'])
        self.router.add_api_route('/api/routes/', self.create_route, methods=['POST'])

    async def get_route(self, id: int):
        ...

    async def create_route(self, route: Annotated[RouteAdd, Depends()], format: str = 'csv'):
        ...

    async def ping(self):
        ...
