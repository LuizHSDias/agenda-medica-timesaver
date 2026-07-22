from app import create_app

# Cria a aplicação Flask utilizando o padrão Application Factory
app = create_app()


if __name__ == "__main__":
    # Inicia o servidor da aplicação
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )