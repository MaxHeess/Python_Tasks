a = int(input("Alter"))
v = input("A)bendvorstellung, S)pätvorstellung, N)achmittagsvorstellung")
# Beim Einlesen von Variablen auf der Konsole wird automatisch ein String eingelesen, also eine Zeichenkette
# "1" = Ziffer 1    1 = Zahl 1.

if (a < 15) and (v == "a"):
    print("Zahlen Sie 8 EUR")
if (a < 15) and (v == "s"):
    print("kein Zutritt")
if (a < 15) and (v == "n"):
    print("Zahlen Sie 6 EUR")
if (a > 14) and (v == "a" ):
    print("Zahlen Sie 12 EUR")
if (a > 14) and (v == "s"):
    print("Zahlen Sie 8 EUR")
if (a < 14) and (v == "n"):
    print("Zahlen Sie 10 EUR")