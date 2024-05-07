import os

from sqlalchemy.ext.asyncio import (AsyncSession, create_async_engine,
                                    async_sessionmaker
                                    )

from database.models import BaseClient

engine = create_async_engine(
    os.getenv('DATABASE'),
    future=True, echo=True
    )

session_maker = async_sessionmaker(
    engine, class_=AsyncSession,
    expire_on_commit=False
    )


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseClient.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseClient.metadata.drop_all)
