def schaltjahr(jahr):
    if ((jahr % 4 == 0) and not (jahr % 100 == 0) or (jahr% 4 == 0) and (jahr % 100 == 0) and (jahr % 400 == 0)):
        return True
    else:
        return False

j = int(input("Jahreszahl: "))
if schaltjahr(j):
    print("Schaltjahr")
else:
    print("kein Schaltjahr")

