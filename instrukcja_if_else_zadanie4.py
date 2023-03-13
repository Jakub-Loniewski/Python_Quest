math_grade = int(input("Jaka jest twoja ocena z matematyki"))
physics_grade = int(input("Jaka jest twoja ocena z fizyki"))
polish_grade = int(input("Jaka jest twoja ocena z polskiego"))
english_grade = int(input("Jaka jest twoja ocena z angielskiego"))
history_grade = int(input("Jaka jest twoja ocena z hisorii"))

numbers_of_failures = 0

if math_grade < 2:
    numbers_of_failures = numbers_of_failures + 1
if physics_grade < 2:
    numbers_of_failures = numbers_of_failures + 1
if polish_grade < 2:
    numbers_of_failures = numbers_of_failures + 1
if english_grade < 2:
    numbers_of_failures = numbers_of_failures + 1
if history_grade < 2:
    numbers_of_failures = numbers_of_failures + 1

if numbers_of_failures == 0:
    print("Gratulacje zdałeś/zdałaś do następnej Klasy")
else:
    if numbers_of_failures == 1:
        average = (math_grade + physics_grade + polish_grade + english_grade + history_grade) / 5
        if average > 3.5:
            print("gratulacje zdałeś/zdałaś do następnej Klasy")
        else:
            print("niestety...")
    else:
        print("niestety...")
