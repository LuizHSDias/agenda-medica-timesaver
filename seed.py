from werkzeug.security import generate_password_hash
from app import create_app
from app.extensions import db
from app.models.user import User

# Cria a aplicação Flask
app = create_app()

with app.app_context():

    # Verifica se o usuário administrador já existe
    user = User.query.filter_by(email="admin@timesaver.com").first()

    if user is None:

        # Cria o usuário administrador padrão
        user = User(
            name="Administrador",
            email="admin@timesaver.com",
            password=generate_password_hash("123456")
        )

        db.session.add(user)
        db.session.commit()

        # Exibe as credenciais criadas
        print("======================================")
        print("Usuário administrador criado com sucesso!")
        print("E-mail: admin@timesaver.com")
        print("Senha: 123456")
        print("======================================")

    else:

        # Informa que o usuário já está cadastrado
        print("======================================")
        print("Usuário já existe.")
        print("E-mail: admin@timesaver.com")
        print("Senha: 123456")
        print("======================================")