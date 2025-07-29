import os
from dotenv import load_dotenv

load_dotenv()

class DBConfig:
    def __init__(self):
        self.db_type = os.getenv("DB_TYPE", "postgres")
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = os.getenv("DB_PORT", 5432)
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD", "postgres")
        self.db_name = os.getenv("DB_NAME", "mydb")

    def get_sync_url(self):
        if self.db_type == "postgres":
            return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        raise NotImplementedError("Unsupported sync DB")

    def get_async_url(self):
        if self.db_type == "postgres":
            return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        raise NotImplementedError("Unsupported async DB")
