# Używamy oficjalnego, stabilnego obrazu Pythona
FROM python:3.12

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiujemy listę paczek i je instalujemy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę naszego kodu (main.py, models.py, database.py)
COPY . .

# Wystawiamy port i uruchamiamy serwer
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]