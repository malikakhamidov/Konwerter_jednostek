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
