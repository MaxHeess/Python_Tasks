#Aufgabe1
i = 0
while i <= 10:
    print(i, end = "," if i < 10 else "\n")
    i = i + 1

#Aufgabe2
i = -10
while i <= 10:
    print(i, end = "," if i < 10 else "\n")
    i = i + 2

#Aufgabe3
n = 0
i = n ** 2
while i < 100:
    print(i, end = "," if i < 81 else "\n")
    n +=  1
    i = n ** 2

#Aufgabe4
i = 1
while i < 200:
    print(i, end = "," if i < 128 else "\n")
    i =  i * 2

#Aufgabe5
n = 0
i = 1
while i < 16:
    print(n, end = ",")
    n +=  i
    i += 1