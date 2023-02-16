shopping_elements = input("Wprowadź listę zakupów po przecinkach,")
shopping_list = shopping_elements.split(",")

is_shopping_list_long = len(shopping_list) >4
print(f"czy ważam, ze twoja lista zakupów jest długa? {is_shopping_list_long}")