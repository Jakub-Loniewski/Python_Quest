print("wypisz ceny samochodów porównamy je")

bmw_m5 = float(input("wypisz cenę m5 na otomoto : "))
bmw_m3 = float(input("wypisz cenę m3 na otomoto : "))
bmw_m6 = float(input("wypisz cenę m6 na otomoto : "))


if bmw_m5 > bmw_m3 :
    print("Bmw m5 jest droższa od bmw m3")
else:
    print("Bmw m5 nie jest droższe od bmw m3")

if bmw_m3 < bmw_m6:
    print("Bmw m3 jest tańsza niż bmw m6")

else:
    print("bmw m3 nie jest tańsza niż bmw m6")

if bmw_m5 == bmw_m6:
    print("Bmw m5 i bmw m6 kosztują tyle samo")

else:
    print("bmw m5 i bmw m6 nie kosztuja tyle samo")

