from pydantic import BaseModel, ConfigDict


class Point(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    lat: float
    lng: float

