print("ile miesięcznie wydajesz na")
food = float(input("jedzenie? "))
fun = float(input("rozrywka? "))
bills = float(input("opłaty?"))
other = float(input("inne ?"))

total_expenditures = food + fun + bills + other
expenditures_percentage = {
    "jedzenie": food * 100 / total_expenditures,
    "rozrywka": fun * 100 / total_expenditures,
    "opłaty": bills * 100/ total_expenditures,
    "inne": other * 100/total_expenditures,
    }
selected_category = input("wybierz jedną z kategorii wydatków (jedzenie/rozrywka/opłaty/inne:")
print(f"Na {selected_category} wydajesz {expenditures_percentage[selected_category]:.0f}% wszystkich wydatków")