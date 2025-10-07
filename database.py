from sqlalchemy import create_engine
import os

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DB_URL,
    connect_args={"sslmode": "require"},
    echo=True,
)
