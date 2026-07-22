from flask import Flask, jsonify

app = Flask(__name__)

# Lista simulando os dados retornados por uma API
appointments = [
    {
        "id": 1,
        "paciente": "João Silva",
        "cpf": "123.456.789-00",
        "medico": "Dra. Ana Costa",
        "especialidade": "Cardiologia",
        "data": "2026-07-23",
        "horario": "09:00",
        "convenio": "Unimed",
        "status": "Confirmado"
    },
    {
        "id": 2,
        "paciente": "Maria Oliveira",
        "cpf": "987.654.321-00",
        "medico": "Dr. Carlos Lima",
        "especialidade": "Dermatologia",
        "data": "2026-07-23",
        "horario": "10:30",
        "convenio": "Bradesco Saúde",
        "status": "Confirmado"
    },
    {
        "id": 3,
        "paciente": "Pedro Santos",
        "cpf": "111.222.333-44",
        "medico": "Dra. Juliana Rocha",
        "especialidade": "Pediatria",
        "data": "2026-07-24",
        "horario": "14:00",
        "convenio": "SulAmérica",
        "status": "Pendente"
    },
    {
        "id": 4,
        "paciente": "Fernanda Souza",
        "cpf": "555.666.777-88",
        "medico": "Dr. Ricardo Mendes",
        "especialidade": "Ortopedia",
        "data": "2026-07-24",
        "horario": "15:30",
        "convenio": "Unimed",
        "status": "Confirmado"
    },
    {
        "id": 5,
        "paciente": "Lucas Almeida",
        "cpf": "222.333.444-55",
        "medico": "Dra. Camila Freitas",
        "especialidade": "Neurologia",
        "data": "2026-07-25",
        "horario": "08:00",
        "convenio": "Amil",
        "status": "Cancelado"
    },
    {
        "id": 6,
        "paciente": "Carla Mendes",
        "cpf": "999.888.777-66",
        "medico": "Dr. Eduardo Martins",
        "especialidade": "Ginecologia",
        "data": "2026-07-25",
        "horario": "11:00",
        "convenio": "Hapvida",
        "status": "Confirmado"
    }
]


@app.route("/")
def home():
    # Exibe uma mensagem informando os endpoints disponíveis
    return {
        "message": "Mock API da Agenda Médica",
        "endpoint": "/appointments"
    }


@app.get("/appointments")
def get_appointments():
    """
    Retorna a lista de agendamentos.
    """

    # Retorna os dados em formato JSON
    return jsonify(appointments)


if __name__ == "__main__":
    # Inicia a aplicação Flask
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )