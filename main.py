from converter.length import (
    cm_to_m, m_to_cm, cm_to_inch, inch_to_cm,
    cm_to_km, km_to_cm, cm_to_feet, feet_to_cm,
    km_to_mile, mile_to_km
)
from converter.mass import (
    g_to_kg, kg_to_g, kg_to_t, t_to_kg,
    mg_to_kg, kg_to_mg, mg_to_g, g_to_mg,
    kg_to_lb, lb_to_kg
)
from converter.temperature import (
    c_to_f, c_to_k, f_to_c, f_to_k, k_to_c, k_to_f
)


def get_int(prompt, min_val, max_val):
    """Pyta o liczbę całkowitą dopóki użytkownik nie poda poprawnej."""
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Podaj liczbę od {min_val} do {max_val}.")
        except ValueError:
            print("To nie jest liczba całkowita. Spróbuj ponownie.")


def get_float(prompt):
    """Pyta o liczbę zmiennoprzecinkową dopóki użytkownik nie poda poprawnej."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")


def menu_length():
    opcje = {
        1:  ("Centymetr → Metr",      cm_to_m,    "cm",  "m"),
        2:  ("Metr → Centymetr",      m_to_cm,    "m",   "cm"),
        3:  ("Centymetr → Cal",       cm_to_inch, "cm",  "cal"),
        4:  ("Cal → Centymetr",       inch_to_cm, "cal", "cm"),
        5:  ("Centymetr → Kilometr",  cm_to_km,   "cm",  "km"),
        6:  ("Kilometr → Centymetr",  km_to_cm,   "km",  "cm"),
        7:  ("Centymetr → Stopa",     cm_to_feet, "cm",  "ft"),
        8:  ("Stopa → Centymetr",     feet_to_cm, "ft",  "cm"),
        9:  ("Kilometr → Mila",       km_to_mile, "km",  "mil"),
        10: ("Mila → Kilometr",       mile_to_km, "mil", "km"),
    }

    print("\n>>> Konwersja długości")
    for k, (nazwa, *_) in opcje.items():
        print(f"{k:2}. {nazwa}")

    wybor = get_int("Wybierz konwersję (1-10): ", 1, 10)
    wartosc = get_float("Podaj wartość: ")

    nazwa, funkcja, jednostka_z, jednostka_na = opcje[wybor]
    wynik = funkcja(wartosc)
    print(f"\nWynik: {wartosc} {jednostka_z} = {wynik:.4f} {jednostka_na}")


def menu_mass():
    opcje = {
        1:  ("Gram → Kilogram",       g_to_kg,  "g",  "kg"),
        2:  ("Kilogram → Gram",       kg_to_g,  "kg", "g"),
        3:  ("Kilogram → Tona",       kg_to_t,  "kg", "t"),
        4:  ("Tona → Kilogram",       t_to_kg,  "t",  "kg"),
        5:  ("Miligram → Kilogram",   mg_to_kg, "mg", "kg"),
        6:  ("Kilogram → Miligram",   kg_to_mg, "kg", "mg"),
        7:  ("Miligram → Gram",       mg_to_g,  "mg", "g"),
        8:  ("Gram → Miligram",       g_to_mg,  "g",  "mg"),
        9:  ("Kilogram → Funt",       kg_to_lb, "kg", "lb"),
        10: ("Funt → Kilogram",       lb_to_kg, "lb", "kg"),
    }

    print("\n>>> Konwersja masy")
    for k, (nazwa, *_) in opcje.items():
        print(f"{k:2}. {nazwa}")

    wybor = get_int("Wybierz konwersję (1-10): ", 1, 10)
    wartosc = get_float("Podaj wartość: ")

    nazwa, funkcja, jednostka_z, jednostka_na = opcje[wybor]
    wynik = funkcja(wartosc)
    print(f"\nWynik: {wartosc} {jednostka_z} = {wynik:.4f} {jednostka_na}")


def menu_temperature():
    opcje = {
        1: ("Celsjusz → Fahrenheit",  c_to_f, "°C", "°F"),
        2: ("Celsjusz → Kelvin",      c_to_k, "°C", "K"),
        3: ("Fahrenheit → Celsjusz",  f_to_c, "°F", "°C"),
        4: ("Fahrenheit → Kelvin",    f_to_k, "°F", "K"),
        5: ("Kelvin → Celsjusz",      k_to_c, "K",  "°C"),
        6: ("Kelvin → Fahrenheit",    k_to_f, "K",  "°F"),
    }

    print("\n>>> Konwersja temperatury")
    for k, (nazwa, *_) in opcje.items():
        print(f"{k:2}. {nazwa}")

    wybor = get_int("Wybierz konwersję (1-6): ", 1, 6)
    wartosc = get_float("Podaj wartość: ")

    nazwa, funkcja, jednostka_z, jednostka_na = opcje[wybor]
    wynik = funkcja(wartosc)
    print(f"\nWynik: {wartosc} {jednostka_z} = {wynik:.4f} {jednostka_na}")


def main():
    print("Konwerter jednostek")
    print("===================")

    while True:
        print("\n--- Menu główne ---")
        print(" 1. Długość")
        print(" 2. Masa")
        print(" 3. Temperatura")
        print(" 4. Wyjdź")

        wybor = get_int("Wybierz kategorię (1-4): ", 1, 4)

        if wybor == 1:
            menu_length()
        elif wybor == 2:
            menu_mass()
        elif wybor == 3:
            menu_temperature()
        elif wybor == 4:
            print("Do widzenia!")
            break


if __name__ == "__main__":
    main()
