from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

def test_login_valido(client, app):

    with app.app_context():

        # Cria um usuário para realizar o teste de autenticação
        db.create_all()

        user = User(
            name="Administrador",
            email="admin@teste.com",
            password=generate_password_hash("123456"),
        )

        db.session.add(user)
        db.session.commit()

    # Envia uma requisição de login com credenciais válidas
    response = client.post(
        "/login",
        data={
            "email": "admin@teste.com",
            "password": "123456",
        },
        follow_redirects=False,
    )

    # Verifica se o usuário foi redirecionado para a agenda
    assert response.status_code == 302
    assert "/agenda" in response.headers["Location"]


def test_login_invalido(client, app):

    with app.app_context():

        # Cria um usuário para validar a autenticação
        db.create_all()

        user = User(
            name="Administrador",
            email="admin@teste.com",
            password=generate_password_hash("123456"),
        )

        db.session.add(user)
        db.session.commit()

    # Envia uma requisição com senha incorreta
    response = client.post(
        "/login",
        data={
            "email": "admin@teste.com",
            "password": "senhaerrada",
        },
        follow_redirects=True,
    )

    # Verifica se a aplicação permaneceu na tela de login
    # e exibiu a mensagem de erro
    assert response.status_code == 200
    assert b"Usu\xc3\xa1rio ou senha inv\xc3\xa1lidos" in response.data