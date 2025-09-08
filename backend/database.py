import os


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import declarative_base


from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "sqlite+aiosqlite:///wholesale_marketplace.db"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

async_sessionLocal = async_sessionmaker(engine, class_=AsyncSession)

Base = declarative_base()


async def get_db():
    async with async_sessionLocal() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)