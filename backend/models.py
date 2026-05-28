from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String, index=True)      # Pełna nazwa, np. "dolar amerykański"
    code = Column(String, index=True)          # Kod waluty, np. "USD"
    mid = Column(Float)                        # Średni kurs, np. 3.95
    effective_date = Column(Date, index=True)  # Data publikacji kursu z NBP