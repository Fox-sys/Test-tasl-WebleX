from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config import Config

engine = create_async_engine(
    Config().get_async_connection()
)

new_session = async_sessionmaker(engine, expire_on_commit=False)
