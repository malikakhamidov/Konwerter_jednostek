[![CI](https://github.com/malikakhamidov/Konwerter_jednostek/actions/workflows/ci.yml/badge.svg)](https://github.com/malikakhamidov/Konwerter_jednostek/actions/workflows/ci.yml)

# Konwerter jednostek

Konsolowy konwerter jednostek napisany w Pythonie.

## Funkcje

- Konwersja długości (10 typów)
- Konwersja masy (10 typów)
- Konwersja temperatury (6 typów)
- Walidacja wejścia — program nie pada przy błędnym inpucie
- Testy jednostkowe z pomiarem pokrycia kodu

## Wymagania

- Python 3.10+
- pytest
- pytest-cov

## Instalacja
```bash
git clone https://github.com/malikakhamidov/Konwerter_jednostek.git
cd Konwerter_jednostek
pip install -r requirements.txt
```

## Uruchomienie
```bash
python main.py
```

## Testy
```bash
# Wszystkie testy
pytest tests/ -v

# Testy z raportem pokrycia
pytest tests/ --cov=converter --cov-report=term-missing

# Próg pokrycia 80% (używany przez CI)
pytest tests/ --cov=converter --cov-fail-under=80
```

## Autorzy

- Eryk Kilarski
- Malika Khamidov
- Marcin Lipowski
