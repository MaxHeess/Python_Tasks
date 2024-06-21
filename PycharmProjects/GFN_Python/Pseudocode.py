e = int(input("Endwert:"))
produkt = 1

for i in range(1, e + 1):
     if i % 5 == 0 and i % 7 == 0:
        produkt = produkt * i
print("Ergebnis:", produkt)

