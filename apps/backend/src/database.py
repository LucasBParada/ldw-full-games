from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


# cria banco se não existir
def create_database():
    server_url = "mysql+pymysql://root@127.0.0.1:3306"
    engine = create_engine(server_url)

    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS full_games"))
        conn.commit()


engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


class Base(DeclarativeBase):
    pass


def init_db():
    from models.host import Host
    from models.game import Game
    from models.player import Player

    Base.metadata.create_all(bind=engine)