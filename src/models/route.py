from typing import List, Dict

from pydantic import BaseModel, ConfigDict

from src.models.point import Point


class RouteAdd(BaseModel):
    ...


class RouteGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    points: List[Point]
