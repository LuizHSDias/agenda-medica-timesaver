from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Instância do banco de dados
db = SQLAlchemy()

# Gerencia a autenticação e as sessões dos usuários
login_manager = LoginManager()

# Redireciona para a tela de login ao acessar uma rota protegida
login_manager.login_view = "auth.login"

# Mensagem exibida quando o usuário não está autenticado
login_manager.login_message = "Faça login para continuar."


@login_manager.user_loader
def load_user(user_id):
    """
    Recupera um usuário pelo ID armazenado na sessão.
    """

    from app.models.user import User

    # Busca o usuário no banco de dados pelo ID
    return db.session.get(User, int(user_id))