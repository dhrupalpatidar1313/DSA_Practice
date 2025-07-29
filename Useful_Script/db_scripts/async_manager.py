from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from .db_config import DBConfig

class AsyncDBManager:
    def __init__(self):
        config = DBConfig()
        self.engine = create_async_engine(config.get_async_url(), echo=False)
        self.AsyncSessionLocal = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self):
        async with self.AsyncSessionLocal() as session:
            yield session

    async def create_record(self, session, model):
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return model
