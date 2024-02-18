from src.core.find_shortest_path import find_shortest_path
from src.models.point import Point
from src.tests.base_test import BaseTest


class Test(BaseTest):
    def get_tests(self):
        return (self.test_1, self.test_2)

    def get_test_name(self):
        return 'test_find_shortest_way'

    def test_1(self):
        assert find_shortest_path(
            [Point(lat=0, lng=0), Point(lat=0, lng=1), Point(lat=-1, lng=-1), Point(lat=2, lng=1)]) == [
                   Point(lat=0, lng=0), Point(lat=-1, lng=-1), Point(lat=0, lng=1), Point(lat=2, lng=1)]

    def test_2(self):
        assert find_shortest_path(
            [Point(lat=-2, lng=-2), Point(lat=2, lng=2), Point(lat=10, lng=10), Point(lat=8, lng=8)]) == [
                   Point(lat=-2, lng=-22), Point(lat=2, lng=2), Point(lat=8, lng=8), Point(lat=10, lng=10)]
