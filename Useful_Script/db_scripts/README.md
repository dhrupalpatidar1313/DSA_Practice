# Universal Python DB Manager

A reusable, modular, and project-agnostic database connection system for Python projects, supporting both **synchronous** (SQLAlchemy) and **asynchronous** (SQLModel) operations.

---

## Features

* **Sync and Async support**: Use either `SyncDBManager` or `AsyncDBManager` based on your application needs.
* **Environment-driven configuration**: Load credentials and settings from a `.env` file via `python-dotenv`.
* **Class-based managers**: Encapsulate connection logic in clean, reusable classes.
* **Model-agnostic**: Plug your own SQLAlchemy or SQLModel models without boilerplate.
* **Auto schema creation**: Create tables automatically via `init_db()` methods.
* **CRUD skeleton**: Basic `create_record()` helper included; extend for full CRUD.

---

## Repository Structure

```
universal_db/
├── config.py           # DBConfig: .env loader + URL builders
├── base.py             # Base classes for SQLAlchemy and SQLModel
├── sync_manager.py     # SyncDBManager: SQLAlchemy engine & session
└── async_manager.py    # AsyncDBManager: async engine & session

models.py               # Example model definitions
main_sync.py            # Sync usage example
main_async.py           # Async usage example
.env                    # Environment variables
README.md               # This documentation
```

---

## Prerequisites

* Python 3.8+
* A PostgreSQL server (or adjust `DBConfig` for other databases)

---

## Installation

1. **Clone** or copy the `universal_db` folder into your project.
2. Install dependencies:

```bash
pip install sqlalchemy asyncpg sqlmodel python-dotenv
```

---

## Configuration

Create a `.env` file in your project root with these variables:

```dotenv
DB_TYPE=postgres
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
```

* **DB\_TYPE**: currently supports `postgres` for both sync and async.
* **DB\_HOST**, **DB\_PORT**, **DB\_USER**, **DB\_PASSWORD**, **DB\_NAME**: your connection credentials.

---

## Components

### 1. `config.py`

Defines `DBConfig`, which loads `.env` and exposes:

* `get_sync_url()`: returns a SQLAlchemy URL (e.g. `postgresql://user:pass@host:port/db`).
* `get_async_url()`: returns an async URL (e.g. `postgresql+asyncpg://user:pass@host:port/db`).

### 2. `base.py`

Provides base classes:

```python
from sqlalchemy.orm import declarative_base
from sqlmodel import SQLModel

Base = declarative_base()    # For sync models
AsyncBase = SQLModel         # For async models (inherit directly)
```

### 3. `sync_manager.py`

Encapsulates sync DB logic:

```python
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
```

* **`init_db()`**: creates tables for all models inheriting from `Base`.
* **`get_session()`**: returns a new SQLAlchemy `Session`.
* **`create_record()`**: helper to add & commit a new record.

### 4. `async_manager.py`

Encapsulates async DB logic:

```python
class AsyncDBManager:
    def __init__(self):
        config = DBConfig()
        self.engine = create_async_engine(config.get_async_url(), echo=False)
        self.AsyncSessionLocal = sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

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
```

* **`init_db()`**: asynchronously creates tables based on all `SQLModel` subclasses.
* **`get_session()`**: async context generator yielding an `AsyncSession`.
* **`create_record()`**: helper to add & commit a new record in async flow.

---

## Usage Examples

### Synchronous Example (`main_sync.py`)

```python
from universal_db.sync_manager import SyncDBManager
from models import User  # SQLAlchemy model inheriting from Base

# Initialize manager and schema
db = SyncDBManager()
db.init_db()

# Create a new session and record
session = db.get_session()
new_user = User(name="Dhrupal", email="dhrupal@example.com")
saved_user = db.create_record(session, new_user)
print(f"Created user with ID: {saved_user.id}")
# Session remains open until explicitly closed or garbage-collected
```

### Asynchronous Example (`main_async.py`)

```python
import asyncio
from universal_db.async_manager import AsyncDBManager
from models import AsyncUser  # SQLModel model

async def main():
    db = AsyncDBManager()
    # Create tables asynchronously
    await db.init_db()

    # Use async context to get session
    async for session in db.get_session():
        new_user = AsyncUser(name="Alice", email="alice@example.com")
        saved_user = await db.create_record(session, new_user)
        print(f"Created user with ID: {saved_user.id}")

if __name__ == "__main__":
    asyncio.run(main())
```

* The `async for` loop ensures proper opening and closing of the `AsyncSession`.
* `init_db()` must be called before any operations to ensure tables exist.

---

## Extensibility

* **Add more DBs**: Extend `DBConfig` to support MySQL, SQLite, etc.
* **CRUD mixins**: Enhance managers with `read`, `update`, `delete` methods.
* **Migrations**: Integrate Alembic for schema versioning.
* **Packaging**: Publish as a PyPI package for global reuse.

---

## License

MIT © dhrupalpatidar1313
