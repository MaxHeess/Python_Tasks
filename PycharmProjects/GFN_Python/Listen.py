#Aufgabe1
#     0, 1, 2, 3, …, 10
ausgabe = []
max = 11
for i in range(0, max):
    ausgabe.append(i)
print(ausgabe)

#Aufgabe2
ausgabe = []
max = 11
for i in range(-10, max, 2):
    ausgabe.append(i)
print(ausgabe)

#Aufgabe3
ausgabe = []
max = 11
for i in range(0, max):
    ausgabe.append(i**2)
print(ausgabe)

#Aufgabe4
ausgabe = []
max = 11
for i in range(0, max):
    ausgabe.append(2**i)
print(ausgabe)

#Aufgabe5
ausgabe = []
max = 11
zahl = 0
for i in range(0, max):
    zahl = zahl + i
    ausgabe.append(zahl)
print(ausgabe)