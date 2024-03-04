# Какой язык программирования
FROM python:latest
# Копируем наш проект внутри Docker
COPY . /paysistem46
# Назначить основную нашу папку для Docker
WORKDIR /paysistem46
# Установка библиотек
RUN pip install -r requirements.txt
# Запуск проекта
CMD ['uvicorn', 'main:app', '--reload',  "--host=0.0.0.0", "--port=2525"]