print("Kalkulator wartosci lokaty z roczna kapitalizacja")

initial_value_input = input("jaka kwotę wpłaciłeś/wpłaciłaś?")
initial_value = int(initial_value_input)
percentage_input = input("jakie jest oprocentowanie (%) ?-")
percentage = int(percentage_input)
years_input = input("ile lat trwa lokata")
years = int(years_input)

final_value = initial_value * (1 + percentage / 100) ** years
print(f"Po {years} latach twoja lokata {final_value :.2f} zł")
