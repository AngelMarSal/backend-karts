from sqlalchemy.orm import String, Enum, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime

# https://docs.sqlalchemy.org/en/20/orm/quickstart.html
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    rol: Mapped[str] = mapped_column(
        Enum('cliente', 'admin', 'operario', name='user_role'),
        default='cliente'
    )
    fecha_registro: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    # el !r incluye comillas, quedaria como {'id': 1, 'email': 'default@gmail.com', 'rol': 'cliente'}
    def __repr__(self) -> str:
        return f'User(id={self.id!r}, email={self.email!r}, rol={self.rol!r})'