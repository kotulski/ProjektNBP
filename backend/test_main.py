from fastapi.testclient import TestClient
from main import app
from datetime import date

# Tworzymy wirtualnego klienta, który będzie "odpytywał" nasze API w testach
client = TestClient(app)

def test_fetch_currencies_from_nbp():
    """Testuje, czy endpoint POST pobiera dane z NBP i poprawnie zapisuje je do bazy."""
    response = client.post("/currencies/fetch")
    
    # Oczekujemy, że serwer odpowie statusem 200 OK
    assert response.status_code == 200
    
    # Oczekujemy, że w odpowiedzi znajdzie się słowo "Pomyślnie" (co oznacza udany zapis)
    assert "Pomyślnie" in response.json()["message"]

def test_get_all_currencies():
    """Testuje, czy endpoint GET zwraca listę walut."""
    response = client.get("/currencies")
    
    assert response.status_code == 200
    # Oczekujemy, że odpowiedź to lista (tablica JSON)
    assert isinstance(response.json(), list)
    # Po wcześniejszym teście lista nie powinna być pusta
    assert len(response.json()) > 0

def test_get_currencies_by_date():
    """Testuje, czy endpoint GET poprawnie wyszukuje kursy po dacie."""
    # Używamy dzisiejszej daty, bo wiemy, że przed chwilą pobraliśmy najświeższe dane
    today_str = date.today().strftime("%Y-%m-%d")
    
    response = client.get(f"/currencies/{today_str}")
    
    # API powinno zwrócić 200 (znaleziono dane) albo 404 (jeśli dzisiaj jest np. wolne i NBP nie wydał kursów)
    assert response.status_code in [200, 404]
    
    if response.status_code == 200:
        assert isinstance(response.json(), list)