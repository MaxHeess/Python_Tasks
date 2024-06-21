#Mithilfe einer while-Schleife sollen folgende Zahlenreihen ausgegeben werden
#    • 0, 1, 2, 3, …, 10
#    • -10, -8, -6, …, +10
#    • 0, 1, 4, 9, …
#    • 1, 2, 4, 8, …
#    • 0, 1, 3, 6, 10, 15, … (<100)


#Aufgabe1
#     0, 1, 2, 3, …, 10
ausgabe = ""
i = 1
max = 11
while i < max:
    ausgabe = ausgabe + str(i)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)

#Aufgabe2
#     -10, -8, -6, …, +10
ausgabe = ""
i = -10
max = 11
while i < max:
    ausgabe = ausgabe + str(i)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 2
print(ausgabe)

#Aufgabe3
#    0, 1, 4, 9, …
ausgabe = ""
i = 0
max = 11
while i < max:
    ausgabe = ausgabe + str(i**2)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)

#Aufgabe4
#    1, 2, 4, 8, …
ausgabe = ""
i = 0
max = 11
while i < max:
    ausgabe = ausgabe + str(2**i)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)

#Aufgabe5
#    0, 1, 3, 6, 10, 15, …
ausgabe = ""
i = 0
max = 11
zahl = 0
while i < max:
    zahl = zahl + i
    ausgabe = ausgabe + str(zahl)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)