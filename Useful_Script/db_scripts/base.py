from sqlalchemy.orm import declarative_base
from sqlmodel import SQLModel

Base = declarative_base()  # For SQLAlchemy
AsyncBase = SQLModel       # For SQLModel (used directly)
