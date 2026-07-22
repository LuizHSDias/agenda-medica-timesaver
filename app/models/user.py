from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class User(UserMixin, db.Model):
    """
    Modelo que representa um usuário do sistema.
    """

    __tablename__ = "users"

    # Chave primária
    id: Mapped[int] = mapped_column(primary_key=True)

    # Nome do usuário
    name: Mapped[str] = mapped_column(nullable=False)

    # E-mail único utilizado no login
    email: Mapped[str] = mapped_column(unique=True, nullable=False)

    # Senha criptografada
    password: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"