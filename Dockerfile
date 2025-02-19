FROM python:3.12.3-slim

# Instala o Miniconda manualmente
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh

# Adiciona Conda ao PATH
ENV PATH="/opt/conda/bin:$PATH"

# Adiciona channels do conda-forge 
RUN conda config --append channels conda-forge

# Copia o arquivo de dependências Conda
COPY requirements.txt requirements.txt

# Cria e ativa o ambiente Conda
#RUN conda install --file requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

RUN mkdir data \
    && cd data

COPY /src /app/
COPY /data /app/data/

EXPOSE 7878

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["gradio", "app_green_flow.py"]