print("Konwerter jednostek")
print("===================")

# ==== wybór typu konwersji ====
unit_change = \
    {
        1: "Długość",
        2: "Waga",
        3: "Temperatura",
        4: "Wyjdź z programu"
    }
for keys, values in unit_change.items():
    print("{:2}. {}".format(keys, values))

change = int(input("\nWybierz typ jednostek, które chcesz przekształcić: "))

# ==== 1 (Długość) ====
if change == 1:
    print("\n>>> Konwersja długości")
    print("")
    length_dict = \
        {
            1: "Centymetr na Metr",
            2: "Metr na Centymetr",
            3: "Centymetr na Cal",
            4: "Cal na Centymetr",
            5: "Centymetr na Kilometr",
            6: "Kilometr na Centimetr",
            7: "Centymetr na Stopa",
            8: "Stopa na Centymetr",
            9: "Kilometr na Mila",
            10: "Mila na Kilometr",
        }

    # ==== wartość do konwersji ====
    print("==========================")
    length_value = float(input("- Wpisz wartość do konwersji: "))
    for keys, values in length_dict.items():
        print("{:2}. {}".format(keys, values))
    length_convert = int(input("\nWybierz jednostki, z których i na jakie chcesz konwertować. Wpisz wartość od 1 do 10: "))

    # ==== konwersja ====
    if length_convert == 1:
        print("{} cm is equal to {} m.".format(length_value, length_value / 100))
    elif length_convert == 2:
        print("{} m is equal to {} cm.".format(length_value, length_value * 100))
    elif length_convert == 3:
        print("{} cm is equal to {} inch.".format(length_value, length_value / 2.54))
    elif length_convert == 4:
        print("{} inch is equal to {} cm.".format(length_value, length_value * 2.54))
    elif length_convert == 5:
        print("{} cm is equal to {} km.".format(length_value, length_value / 100000))
    elif length_convert == 6:
        print("{} km is equal to {} cm.".format(length_value, length_value * 100000))
    elif length_convert == 7:
        print("{} cm is equal to {} feet.".format(length_value, length_value / 30.48))
    elif length_convert == 8:
        print("{} feet is equal to {} cm.".format(length_value, length_value * 30.48))
    elif length_convert == 9:
        print("{} KM is equal to {} mile".format(length_value, length_value / 1.609))
    elif length_convert == 10:
        print("{} mile is equal to {} KM".format(length_value, length_value * 1.609))
    else:
        print("Wpisz wartość od 1 do 10.")
# ==== 2 (Waga) ====
elif change == 2:
    print("\n>>> Konwersja masy")
    print("")
    mass_dict = \
        {
            1: "Gram na Kilogram",
            2: "Kilogram na Gram",
            3: "Kilogram na Tona",
            4: "Tona na Kilogram",
            5: "Miligram na Kilogram",
            6: "Kilogram na Miligram",
            7: "Miligram na Gram",
            8: "Gram na Miligram",
            9: "Kilogram na Funt (lb)",
            10: "Funt (lb) na Kilogram",
        }

    # ==== wartość do konwersji ====
    print("==========================")
    mass_value = float(input("- Wpisz wartość do konwersji: "))
    for keys, values in mass_dict.items():
        print("{:2}. {}".format(keys, values))
    mass_convert = int(input("\nWybierz jednostki, z których i na jakie chcesz konwertować. Wpisz wartość od 1 do 10: "))

    # ==== konwersja ====
    if mass_convert == 1:
        print("{} g to {} Kg".format(mass_value, mass_value / 1000))
    elif mass_convert == 2:
        print("{} Kg to {} g".format(mass_value, mass_value * 1000))
    elif mass_convert == 3:
        print("{} kg to {} T".format(mass_value, mass_value / 1000))
    elif mass_convert == 4:
        print("{} T to {} kg".format(mass_value, mass_value * 1000))
    elif mass_convert == 5:
        print("{} mg to {} kg".format(mass_value, mass_value / 1000000))
    elif mass_convert == 6:
        print("{} Kg to {} mg".format(mass_value, mass_value * 1000000))
    elif mass_convert == 7:
        print("{} mg to {} g".format(mass_value, mass_value / 1000))
    elif mass_convert == 8:
        print("{} g to {} mg".format(mass_value, mass_value * 1000))
    elif mass_convert == 9:
        print("{} Kg to {} lb".format(mass_value, mass_value * 2.20462))
    elif mass_convert == 10:
        print("{} lb to {} kg".format(mass_value, mass_value / 2.20462))
    else:
        print("Wpisz wartość od 1 do 10.")

# ==== 3 (Temperatura) ====
elif change == 3:
    print("\n>>> Konwersja temperatury")
    print("")
    Temp_dict = \
        {
            1: "Celsiusz na Fahrenheit",
            2: "Celsiusz na Kelvin",
            3: "Fahrenheit na Celsiusz",
            4: "Fahrenheit na Kelvin",
            5: "Kelvin na Celsiusz",
            6: "Kelvin na Fahrenheit"
        }

    # ==== wartość do konwersji ====
    print("==========================")
    Temp_value = float(input("- Wpisz wartość do konwersji: "))
    for keys, values in Temp_dict.items():
        print("{:2}. {}".format(keys, values))
    Temp_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

    # ==== konwersja ====
    if Temp_convert == 1:
        print("{} C to {} F".format(Temp_value, (Temp_value * 9.5) + 32))
    elif Temp_convert == 2:
        print("{} C to {} K".format(Temp_value, Temp_value + 273.15))
    elif Temp_convert == 3:
        print("{} F to {} C".format(Temp_value, (Temp_value - 32) * 5.9))
    elif Temp_convert == 4:
        print("{} C to {} K".format(Temp_value, (Temp_value - 32) * 5.9 + 273.15))
    elif Temp_convert == 5:
        print("{} K to {} C".format(Temp_value, Temp_value - 273.15))
    elif Temp_convert == 6:
        print("{} K to {} F".format(Temp_value, (Temp_value - 273.15) * 9.5 + 32))
    else:
        print("Wpisz wartość od 1 do 10.")


elif change == 4:
    print("\n>>> Wyjście z programu")
    exit()
