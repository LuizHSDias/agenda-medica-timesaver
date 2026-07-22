from flask import Blueprint, render_template
from flask_login import login_required
from app.services.appointment_service import AppointmentService

# Blueprint responsável pelas rotas da agenda
agenda_bp = Blueprint("agenda", __name__)

@agenda_bp.route("/agenda")
@login_required
def index():
    # Busca os agendamentos por meio da camada de serviço
    appointments, error = AppointmentService.get_appointments()

    # Renderiza a página da agenda com os dados obtidos
    return render_template(
        "agenda.html",
        appointments=appointments,
        error=error
    )