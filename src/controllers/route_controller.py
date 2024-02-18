import csv, io
from typing import List, Dict

from fastapi import APIRouter, UploadFile

from src.config import Config
from src.core.find_shortest_path import find_shortest_path
from src.models.point import Point
from src.models.route import RouteAdd, RouteGet
from src.repositories.route_repository import RouteRepository
from src.sqlalchemy_db.tables import RouteTable


class RouteController:
    def __init__(self):
        self.router = APIRouter(prefix='/api/routes')
        self.router.add_api_route('/ping/', self.ping, methods=['GET'])
        self.router.add_api_route('/{id}/', self.get_route, methods=['GET'])
        self.router.add_api_route('/', self.create_route, methods=['POST'])

    async def get_route(self, id: int) -> RouteGet:
        return await RouteRepository.get_by_id(id)

    async def create_route(self, file: UploadFile = None, format: str | None = None) -> RouteGet | Dict:
        if format == 'csv':
            data = await file.read()
            reader = csv.reader(io.StringIO(data.decode()))
            points = [Point(**(lambda r: {'lat': float(r[1]), 'lng': float(r[2])})(row)) for row in list(reader)[1:]]
            Config().set_active_csv(points)
        if Config().ACTIVE_CSV is None:
            return {'error': 'Используйте ?format=csv, что бы добавить новый файл'}
        optimal_way = find_shortest_path(Config().ACTIVE_CSV)
        route = RouteAdd()
        route_id = await RouteRepository.add(route, optimal_way)
        route = await RouteRepository.get_by_id(route_id)
        return RouteGet(id=route.id, points=optimal_way)

    async def ping(self):
        return 'pong'
