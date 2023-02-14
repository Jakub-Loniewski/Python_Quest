biedronka_input = input(" po ile sa jablka w biedronce")
biedronka = int(biedronka_input)
print("biedronka",biedronka, "zł/kg")

lidl_input = input(" po ile sa jablka w lidlu")
lidl = int(lidl_input)
print("lidl", lidl, "zł/kg")

zabka_input = input(" po ile sa jablka w zabce")
zabka = int(zabka_input)
print("zabka",zabka,"zł/kg")

najtansze = min(biedronka,lidl,zabka)

print("najtansze jabkłka są po ",najtansze, "zł/kg")