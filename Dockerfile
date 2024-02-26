# Используем базовый образ Python
FROM python:3.10.12

# Установка рабочей директории внутри контейнера
WORKDIR /usr/src/app

# Копируем файлы зависимостей проекта и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта внутрь контейнера
COPY . .

# Запускаем Flask-приложение
CMD ["python", "app.py"]
