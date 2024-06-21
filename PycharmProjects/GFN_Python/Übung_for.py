#Aufgabe1
i = 0
for i in range(11):
    print(i, end = "," if i < 10 else "\n")

#Aufgabe2
i = -10
for i in range(-10, 11, 2):
    print(i, end = "," if i < 10 else "\n")

#Aufgabe3
ausgabe = ""
i = 0
max = 11
for i in range(i, max):
    ausgabe = ausgabe + str(i**2)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)

#Aufgabe4
ausgabe = ""
i = 0
max = 11
for i in range(i, max):
    ausgabe = ausgabe + str(2**i)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)

#Aufgabe5
ausgabe = ""
i = 0
max = 11
zahl = 0
for i in range(i, max):
    zahl = zahl + i
    ausgabe = ausgabe + str(zahl)
    if i < max - 1:
        ausgabe = ausgabe + ","
    i = i + 1
print(ausgabe)





