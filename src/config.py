from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    _instance = None

    def __init__(self):
        env = environ.Env(
            DEBUG=(bool, False),
            POSTGRES_LOGIN=(str, ''),
            POSTGRES_PASS=(str, ''),
            POSTGRES_DATABASE=(str, ''),
            POSTGRES_HOST=(str, ''),
            POSTGRES_PORT=(int, ''),
        )

        environ.Env.read_env(BASE_DIR / '.env')
        self.DEBUG = env('DEBUG')
        self.POSTGRES_LOGIN = env('POSTGRES_LOGIN')
        self.POSTGRES_PASS = env('POSTGRES_PASS')
        self.POSTGRES_DATABASE = env('POSTGRES_DATABASE')
        self.POSTGRES_HOST = env('POSTGRES_HOST')
        self.POSTGRES_PORT = env('POSTGRES_PORT')
        self.BASE_DIR = BASE_DIR

    def get_async_connection(self):
        return (f'postgresql+asyncpg://{self.POSTGRES_LOGIN}:{self.POSTGRES_PASS}@'
                f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}')

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
