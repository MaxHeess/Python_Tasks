a=int(input("Endwert: "))
ergebnis = 1

for i in range(1,a,1):
    if (i % 5 == 0) and  (i % 7 == 0):
        ergebnis = ergebnis * i
        print(i)
print(ergebnis)