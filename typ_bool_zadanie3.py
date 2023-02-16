print("kalkulator wartości lokaty z roczną kapitalizacja")

initial_value_input = input("jaką wartość wpłaciłeś/wpłaciłaś? ")
initial_value = int(initial_value_input)
percentage_input = input("jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("ile lat trwa lokata? ")
years = int(years_input)

final_value = initial_value * (1 + percentage /100) ** years
capital_growth = final_value - initial_value
capital_growth_percentage = (capital_growth / initial_value) * 100

print( "Po", years, "latach twoja lokata bedzie warta ", final_value)
print(f"czy wartość twojej lokaty wzrosnie w tym czasie o 10% lub wiecej {capital_growth_percentage >=10}")

