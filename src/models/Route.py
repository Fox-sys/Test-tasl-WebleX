from typing import List, Dict

from pydantic import BaseModel

from src.models.Point import Point


class RouteAdd(BaseModel):
    points: List[Point]


class RouteGet(BaseModel):
    id: int
    points: List[Point]
