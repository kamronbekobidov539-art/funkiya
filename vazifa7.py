matn = input("So'z kiriting: ")
natija = {}
for i in matn:
    natija[i] = natija.get(i, 0) + 1
print(natija)
