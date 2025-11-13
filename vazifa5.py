N = int(input("N = "))
sonlar = []
for i in range(N):
    sonlar.append(int(input(f"{i+1}-sonni kiriting: ")))
for i in sonlar[:]:
    if sonlar.count(i) == 1:
        sonlar.remove(i)
print("sonlar =", sonlar)
