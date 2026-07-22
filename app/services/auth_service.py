import logging

from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash

from app.models.user import User

# Configuração de logs
logger = logging.getLogger(__name__)


class AuthService:
    """
    Serviço responsável pela autenticação dos usuários.
    """

    @staticmethod
    def authenticate(email: str, password: str):

        try:
            # Busca o usuário pelo e-mail
            user = User.query.filter_by(email=email).first()

            if not user:
                return None

            # Verifica se a senha informada está correta
            if not check_password_hash(user.password, password):
                return None

            return user

        except SQLAlchemyError:
            logger.exception("Erro ao acessar o banco de dados durante a autenticação.")
            return None