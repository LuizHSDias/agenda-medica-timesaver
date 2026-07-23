from unittest.mock import patch

import requests
from app.services.appointment_service import AppointmentService

def test_api_indisponivel():
    """
    Verifica se a aplicação trata corretamente a indisponibilidade da API.
    """

    # Simula uma falha de conexão com a API
    with patch(
        "app.services.appointment_service.requests.get",
        side_effect=requests.exceptions.ConnectionError,
    ):

        appointments, error = AppointmentService.get_appointments()

    # Verifica se nenhum agendamento foi retornado
    assert appointments == []

    # Verifica se a mensagem de erro foi retornada corretamente
    assert error == "Não foi possível conectar à API."