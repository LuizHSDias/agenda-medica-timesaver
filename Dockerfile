# Imagem oficial do Python utilizada como base
FROM python:3.13-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do projeto para o container
COPY . .

# Expõe a porta utilizada pela aplicação
EXPOSE 5000

# Comando executado ao iniciar o container
CMD ["python", "run.py"]