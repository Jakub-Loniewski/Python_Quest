dishes = input("podaj swoje ulubione dania, rozdziel je przecinkamo: ")
favorite_dishes = dishes.split(",")

dishes_index = 0
while dishes_index <len(favorite_dishes):
    print(f"Ulubione danie numer {dishes_index}: {favorite_dishes[dishes_index]}")
    dishes_index+= 1
