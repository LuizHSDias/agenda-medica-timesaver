# Agenda Médica - TimeSaver Challenge

Sistema web desenvolvido como solução para o desafio técnico da **TimeSaver**.

A aplicação permite que um usuário autenticado visualize uma agenda médica por meio da integração com uma API HTTP simulada. Os agendamentos são apresentados em uma tabela utilizando a biblioteca Tabulator, com funcionalidades de pesquisa e tratamento de cenários de erro.

---

# Tecnologias Utilizadas

- Python 3.13
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- Docker
- Docker Compose
- HTML5
- CSS3
- JavaScript
- Tabulator
- Jinja2
- Requests
- Werkzeug
- Pytest

---

# Funcionalidades

- Autenticação de usuários
- Login e Logout
- Persistência de usuários utilizando SQLite
- Consumo de API REST para obtenção dos agendamentos
- Exibição da agenda utilizando Tabulator
- Pesquisa por paciente
- Pesquisa por CPF
- Pesquisa por médico
- Tratamento de erros da API
- Testes automatizados

---

# Estrutura do Projeto

```text
agenda-medica-timesaver/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── static/
│   ├── templates/
│   ├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── extensions.py
│
├── instance/
│   └── agenda.db
│
├── mock_api/
│   ├── Dockerfile
│   └── app.py
│
├── tests/
│   ├── conftest.py
│   └── test_auth.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
├── seed.py
├── .env.example
├── .gitignore
└── README.md
```

---

# Executando com Docker

## Clonar o repositório

```bash
git clone https://github.com/LuizHSDias/agenda-medica-timesaver.git
cd agenda-medica-timesaver
```

## Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///agenda.db
API_URL=http://mock-api:5001/appointments
```

## Construir e iniciar os containers

```bash
docker compose up --build
```

## Criar o usuário de teste

Após iniciar os containers, execute:

```bash
python seed.py
```

A aplicação estará disponível em:

```
http://localhost:5000
```

A Mock API estará disponível em:

```
http://localhost:5001/appointments
```

---

# Executando Localmente

## Criar o ambiente virtual

### Windows

```bash
python -m venv .venv
```

## Ativar o ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

## Instalar as dependências

```bash
pip install -r requirements.txt
```

## Executar a Mock API

Em um terminal:

```bash
cd mock_api
python app.py
```

## Executar a aplicação principal

Em outro terminal:

```bash
python run.py
```

## Criar o usuário de teste

```bash
python seed.py
```

---

# Usuário de Teste

Após executar o script `seed.py`, será criado automaticamente um usuário administrador.

| Campo | Valor |
|--------|--------|
| E-mail | admin@timesaver.com |
| Senha | 123456 |

Caso o usuário já exista, o script apenas informará essa condição.

---

# Exemplos de Uso

1. Acesse a aplicação em:

```
http://localhost:5000
```

2. Faça login utilizando as credenciais de teste.

3. Após a autenticação, a agenda médica será carregada automaticamente.

4. Utilize o campo de pesquisa para localizar agendamentos por:

- Nome do paciente;
- CPF;
- Nome do médico.

5. Caso nenhum registro seja encontrado, será exibida a mensagem:

```
Nenhum registro encontrado.
```

6. Em caso de indisponibilidade da API, resposta inválida ou erro de comunicação, uma mensagem amigável será apresentada ao usuário.

---

# Variáveis de Ambiente

A aplicação utiliza variáveis de ambiente para armazenar configurações sensíveis.

| Variável | Descrição |
|----------|-----------|
| SECRET_KEY | Chave secreta utilizada pelo Flask |
| DATABASE_URL | Caminho do banco SQLite |
| API_URL | Endereço da API de agendamentos |

As variáveis são carregadas automaticamente utilizando a biblioteca **python-dotenv**.

---

# Executando os Testes

Execute:

```bash
python -m pytest -v
```

Resultado esperado:

```text
tests/test_auth.py::test_login_valido PASSED
tests/test_auth.py::test_login_invalido PASSED
```

Os testes utilizam um banco SQLite em memória, garantindo isolamento entre as execuções.

---

# Decisões Técnicas

Durante o desenvolvimento foram adotadas algumas decisões para melhorar a organização e manutenção da aplicação:

- Utilização do padrão **Application Factory** do Flask.
- Organização das rotas utilizando **Blueprints**.
- Separação da lógica de negócio em uma camada de **Services**.
- Utilização do **Flask-Login** para autenticação.
- Persistência dos usuários utilizando **SQLite**.
- Configuração da aplicação por meio de variáveis de ambiente.
- Consumo da API utilizando a biblioteca **Requests**.
- Mock API executada em um container independente.
- Testes automatizados desenvolvidos com **Pytest**.
- Registro de logs para facilitar a identificação de falhas na comunicação com a API e no acesso ao banco de dados.

---

# Limitações Conhecidas

- A aplicação utiliza **SQLite**, sendo adequada para desenvolvimento e demonstração, mas não para ambientes de produção com múltiplos acessos simultâneos.
- Os dados da agenda médica são fornecidos por uma **Mock API**, não havendo integração com um sistema externo real.
- O gerenciamento de usuários é realizado por meio do script `seed.py`, não existindo funcionalidades de cadastro ou edição de usuários pela interface.

---

# Autor

**Luiz Henrique Santos Dias**

GitHub: https://github.com/LuizHSDias