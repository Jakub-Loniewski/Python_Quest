number = int(input("Podaj liczbę parzystą"))
try_number = 1
while try_number < 10 and number % 2 != 0:
    number = int(input("Spróbuj jeszcze raz. Podaj liczbę parzystą:"))
    try_number += 1
else:
    print("Brawo!! ")