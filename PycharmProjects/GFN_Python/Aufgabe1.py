p = float(input("Parkdauer"))
e = int(input("Einkauf"))
# Beim Einlesen von Variablen auf der Konsole wird automatisch ein String eingelesen, also eine Zeichenkette
# "1" = Ziffer 1    1 = Zahl 1.
if (e == 1) or (p < 1):
    print("Parkgebühr beträgt 1 EUR")
elif p < 2:
    print("Parkgebühr beträgt 2 EUR")
elif p < 3:
    print("Parkgebühr beträgt 4 EUR")
else:
    print("Parkgebühr beträgt 6 EUR")
