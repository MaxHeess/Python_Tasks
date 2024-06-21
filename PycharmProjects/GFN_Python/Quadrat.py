a = int(input("Sternanzahl eingeben: "))
zeile = "* " * a
zeileLeer = "* " + "  " * (a - 2) +  "*"
print(zeile)
for i in range(a-2):
    print(zeileLeer)
print(zeile)

