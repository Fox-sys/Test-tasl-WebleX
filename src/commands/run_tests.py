import importlib
import os
from src.config import Config


def get_tests_list() -> list:
    tests = os.listdir(Config().BASE_DIR / 'src' / 'tests')
    tests.remove('__init__.py')
    tests.remove('base_test.py')
    tests.remove('__pycache__')
    edited_tests = []
    for test in tests:
        edited_tests.append(test[:-3:])
    return edited_tests


def entrypoint():
    tests = get_tests_list()
    print(f'Running tests:\n - {"\n - ".join(tests)}')
    for test in tests:
        importlib.import_module(f'src.tests.{test}').Test().do_job()
