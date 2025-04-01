# Define as imagens que serão utilizadas
# Imagem oficial do Python e a distro Alpine que é mais leve deixando o container mais "leve"
FROM python:3.13.2-alpine3.21

# efine um rótulo
LABEL manteiner="https://github.com/rochamrcs"

# Copia os arquivos para dentro do container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

# Define diretorio como pasta de trabalho, aonde os comandos serão executados
WORKDIR /app

# Define a porta em que a aplicação será executada
EXPOSE 8000

# Executa uma série de comandos como criação de diretorios, atualizações e instalação de dependencias para execução do projeto
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-chace --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Define o ambinente virtual padrão, para não precisar referenciar o tempo todo
ENV PATH="/py/bin:$PATH"

# Usuario com poucos previlegios definido como padrão para melhor segurança
USER django-user