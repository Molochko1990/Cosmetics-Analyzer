FROM python:3.12-slim

# Установите зависимые библиотеки
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-rus \
    && rm -rf /var/lib/apt/lists/*  # Убираем кэш

# Установите рабочую директорию
WORKDIR /app

# Устанавливаем Poetry и зависимости
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry install --no-dev

# Копируем код проекта
COPY . /app/




# Запуск приложения с FastAPI через uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
