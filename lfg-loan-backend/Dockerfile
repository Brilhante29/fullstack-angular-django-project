# Use a imagem oficial do Python 3.11 com alpine
FROM python:3.11-alpine

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalando dependências
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiando os arquivos do projeto
COPY . /app/

# Limpeza
RUN apk --purge del .build-deps

# Exponha a porta que o Gunicorn irá rodar
EXPOSE 8000

