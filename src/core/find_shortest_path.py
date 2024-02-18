from typing import List

from src.models.point import Point
from itertools import permutations


def count_distance(p1: Point, p2: Point) -> float:
    return ((p1.lat - p2.lat) ** 2 + (p1.lng - p2.lng) ** 2) ** 0.5


def count_distances(point_list: List[Point]) -> List[float]:
    distances = []
    for i, p1 in enumerate(point_list[0:-1]):
        distances.append(count_distance(p1, point_list[i + 1]))
    return distances


def find_shortest_path(point_list: List[Point]) -> List[Point]:
    variants = permutations(point_list[1:])
    distances = {sum(count_distances([point_list[0]] + list(i))): [point_list[0]] + list(i) for i in variants}
    shortest = sorted(distances.keys())[0]
    return distances[shortest]
