FROM python:3.11-bookworm

COPY requirements.txt /

WORKDIR /

RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python", "main.py" ]