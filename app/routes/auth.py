from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import login_user, logout_user
from app.services.auth_service import AuthService

# Blueprint responsável pelas rotas de autenticação
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET"])
def login():
    # Exibe a página de login
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login_post():
    # Obtém as credenciais enviadas pelo formulário
    email = request.form.get("email")
    password = request.form.get("password")

    # Valida as credenciais do usuário
    user = AuthService.authenticate(email, password)

    # Exibe uma mensagem caso a autenticação falhe
    if user is None:
        flash("Usuário ou senha inválidos.", "danger")
        return redirect(url_for("auth.login"))

    # Cria a sessão do usuário autenticado
    login_user(user)

    # Redireciona para a página da agenda
    return redirect(url_for("agenda.index"))


@auth_bp.route("/logout")
def logout():
    # Encerra a sessão do usuário
    logout_user()

    return redirect(url_for("auth.login"))


@auth_bp.route("/")
def home():
    # Redireciona a rota inicial para a página de login
    return redirect(url_for("auth.login"))