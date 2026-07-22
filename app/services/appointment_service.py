import logging

import requests

from app.config import Config

# Configuração básica de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AppointmentService:
    """
    Serviço responsável por buscar os agendamentos na API.
    """

    API_URL = Config.API_URL

    # Campos obrigatórios definidos no desafio
    REQUIRED_FIELDS = {
        "paciente",
        "cpf",
        "medico",
        "especialidade",
        "data",
        "horario",
        "convenio",
        "status"
    }

    @staticmethod
    def get_appointments():
        """
        Busca os agendamentos na API.
        """

        try:

            response = requests.get(
                AppointmentService.API_URL,
                timeout=5
            )

            response.raise_for_status()

            appointments = response.json()

            # Garante que a resposta seja uma lista
            if not isinstance(appointments, list):
                logger.error("Resposta inválida: a API não retornou uma lista.")
                return [], "Resposta inválida da API."

            # Verifica se não existem agendamentos
            if not appointments:
                logger.info("Nenhum agendamento retornado pela API.")
                return [], None

            # Valida os campos obrigatórios
            for appointment in appointments:

                if not isinstance(appointment, dict):
                    logger.error("Item inválido retornado pela API.")
                    return [], "Resposta inválida da API."

                missing = AppointmentService.REQUIRED_FIELDS - appointment.keys()

                if missing:
                    logger.error(
                        "Campos obrigatórios ausentes: %s",
                        ", ".join(sorted(missing))
                    )
                    return [], (
                        "A resposta da API está incompleta. "
                        "Alguns campos obrigatórios não foram encontrados."
                    )

            return appointments, None

        except requests.exceptions.Timeout:
            logger.error("Tempo limite excedido ao acessar a API.")
            return [], "A API demorou para responder."

        except requests.exceptions.ConnectionError:
            logger.error("Falha de conexão com a API.")
            return [], "Não foi possível conectar à API."

        except requests.exceptions.HTTPError as e:
            logger.error("Erro HTTP: %s", e)
            return [], "A API retornou um erro."

        except ValueError:
            logger.error("Resposta da API não é um JSON válido.")
            return [], "A resposta da API não é um JSON válido."

        except Exception:
            logger.exception("Erro inesperado ao consultar a API.")
            return [], "Ocorreu um erro inesperado."