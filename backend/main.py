from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import requests
from datetime import date, datetime

import models
from database import engine, get_db

# Ta linijka automatycznie tworzy tabele w bazie podczas startu serwera
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NBP Currency API",
    description="API do pobierania i zarządzania kursami walut",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NBP Currency API",
    description="API do pobierania i zarządzania kursami walut",
    version="1.0.0"
)

# KRYTYCZNA ZMIANA: Zezwalamy Angularowi na łączenie się z naszym API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/currencies/fetch")
def fetch_currencies(db: Session = Depends(get_db)):
    """Pobiera najnowsze kursy z API NBP i zapisuje do bazy danych."""
    
    # Odpytanie oficjalnego API NBP
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
    
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Błąd połączenia z NBP API")
    
    data = response.json()[0]
    rates = data['rates']
    table_date_str = data['effectiveDate']
    
    # KRYTYCZNA ZMIANA: Zamiana tekstu na obiekt daty Pythona
    parsed_date = datetime.strptime(table_date_str, "%Y-%m-%d").date()
    
    added_count = 0
    
    for rate in rates:
        # Zabezpieczenie przed zapisaniem dwa razy tych samych kursów
        existing = db.query(models.CurrencyRate).filter(
            models.CurrencyRate.code == rate['code'],
            models.CurrencyRate.effective_date == parsed_date
        ).first()
        
        if not existing:
            new_rate = models.CurrencyRate(
                currency=rate['currency'],
                code=rate['code'],
                mid=rate['mid'],
                effective_date=parsed_date
            )
            db.add(new_rate)
            added_count += 1
            
    db.commit()
    return {"message": f"Pomyślnie pobrano i zapisano {added_count} nowych kursów z dnia {table_date_str}."}

@app.get("/currencies")
def get_all_currencies(db: Session = Depends(get_db)):
    """Zwraca wszystkie kursy walut zapisane w bazie."""
    return db.query(models.CurrencyRate).all()

@app.get("/currencies/{target_date}")
def get_currencies_by_date(target_date: date, db: Session = Depends(get_db)):
    """Zwraca kursy walut dla konkretnej daty (format YYYY-MM-DD)."""
    rates = db.query(models.CurrencyRate).filter(models.CurrencyRate.effective_date == target_date).all()
    
    if not rates:
        raise HTTPException(status_code=404, detail="Brak danych dla podanej daty.")
    return rates