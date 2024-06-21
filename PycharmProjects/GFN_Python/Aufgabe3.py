a = int(input("Alter"))
u = int("26")
b = int(input("Behinderung in %"))
bz = int(input("Betriebszugehörigkeit in Jahren"))

if a < 18:
    print("Urlaub = 30")
if a > 55:
    print("Urlaub = 28")
if b > 50:
    print("Urlaub = Urlaub + 5")
if bz > 10:
    print("Urlaub = Urlaub + 2")
