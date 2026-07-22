import os
from dotenv import load_dotenv

# Carrega as variáveis definidas no arquivo .env
load_dotenv()


class Config:
    # Chave utilizada para proteger sessões e cookies
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    # Configuração do banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///agenda.db"
    )

    # Desabilita um recurso que não é necessário e evita avisos do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # URL da Mock API utilizada para buscar os agendamentos
    API_URL = os.getenv(
        "API_URL",
        "http://127.0.0.1:5001/appointments"
    )


# Configuração utilizada durante os testes automatizados
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"