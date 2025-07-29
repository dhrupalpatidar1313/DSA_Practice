from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .db_config import DBConfig
from .base import Base

class SyncDBManager:
    def __init__(self):
        config = DBConfig()
        self.engine = create_engine(config.get_sync_url(), echo=False)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def init_db(self):
        Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    def create_record(self, session, model):
        session.add(model)
        session.commit()
        session.refresh(model)
        return model
