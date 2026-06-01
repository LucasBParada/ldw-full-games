from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)

    host_id: Mapped[int] = mapped_column(
        ForeignKey("hosts.id")
    )

    name: Mapped[str] = mapped_column(String(150))
    genre: Mapped[str] = mapped_column(String(50))

    host = relationship("Host", back_populates="games")

    players = relationship(
        "Player",
        back_populates="game",
        cascade="all, delete-orphan"
    )