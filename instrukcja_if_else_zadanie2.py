shopping_elements = input("Wprowadź listę zakupów po przecinkach,")
shopping_list = shopping_elements.split(",")

if len(shopping_list) > 4:
    print("twoja lista zakupów jest długa")
else:
    print("twoja lista jest krótka")