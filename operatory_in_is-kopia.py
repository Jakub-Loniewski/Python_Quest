shopping_elements = input("Wprowadź listę zakupów po przecinkach,")
shopping_list = shopping_elements.split(",")

if len(shopping_list) > 4:
    print("twoja lista zakupów jest długa")
else:
    print("twoja lista jest krótka")

    if "bułki" in shopping_elements:
        print(" w liście są bułki")
    else:
        print(" w liście nie ma bułki ")
    if "chleb" in shopping_elements:
        print(" w liście jest chleb")
    else:
        print(" w liście nie ma chleba")