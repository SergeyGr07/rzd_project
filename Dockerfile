# Используем базовый образ Python
FROM ubuntu:latest
RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip python3-dev

COPY . /app

# Установка рабочей директории внутри контейнера
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# Запускаем Flask-приложение
CMD ["python3", "app.py"]
