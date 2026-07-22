from flask import Flask

from app.config import Config
from app.extensions import db, login_manager


# Cria e configura a aplicação Flask
def create_app(config_class=Config):
    app = Flask(__name__)

    # Carrega as configurações da aplicação
    app.config.from_object(config_class)

    # Inicializa as extensões
    db.init_app(app)
    login_manager.init_app(app)

    # Cria as tabelas do banco de dados
    with app.app_context():
        from app.models import User
        db.create_all()

    # Importa os Blueprints (conjunto de rotas)
    from app.routes.auth import auth_bp
    from app.routes.agenda import agenda_bp

    # Registra as rotas na aplicação
    app.register_blueprint(auth_bp)
    app.register_blueprint(agenda_bp)

    return app