age = int(input("Podaj swój wiek "))
gender = str(input("Podaj swoją płeć K/M"))
result = int(input("Podaj uzyskany wynik "))

if age ==8:
    if gender == "M":
        if result >= 2190:
            print("Bardzo dobrze")
        elif result >= 1810:
            print("dobrze")
        elif result >= 1420:
            print("Średnio")
        elif result >= 1050:
            print("Zle")
        else:
            print("Bardzo zle")
    else:
        if result >= 2010:
            print("Bardzo dobrze")
        elif result >= 1670:
            print("Dobrze")
        elif result >= 1320:
            print("Srednio")
        elif result >= 990:
            print("Zle")
        else:
            print("bardzo zle")




