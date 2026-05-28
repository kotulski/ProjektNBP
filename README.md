Projekt NBP - Aplikacja Full-Stack (Angular + FastAPI + PostgreSQL)

Jak uruchomić projekt:

Upewnij się, że masz zainstalowanego i uruchomionego Dockera (Docker Desktop).

Otwórz terminal w głównym folderze projektu (tam, gdzie znajduje się plik docker-compose.yml).

Wpisz komendę: docker compose up --build

Poczekaj na zbudowanie kontenerów i uruchomienie serwerów.

Aplikacja frontendowa będzie dostępna w przeglądarce pod adresem: http://localhost:4200

Dokumentacja API (Swagger) jest dostępna pod adresem: http://localhost:8000/docs

Uwaga: Przy pierwszym uruchomieniu tabela walut jest pusta. Należy kliknąć przycisk pobierania na stronie, aby zainicjować zrzut danych z API NBP do nowej bazy PostgreSQL.