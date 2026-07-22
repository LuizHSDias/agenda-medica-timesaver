import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import db


# Cria uma aplicação configurada para testes
@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        # Cria as tabelas antes da execução dos testes
        db.create_all()

        yield app

        # Remove a sessão e apaga as tabelas após os testes
        db.session.remove()
        db.drop_all()


# Disponibiliza um cliente para simular requisições HTTP
@pytest.fixture
def client(app):
    return app.test_client()