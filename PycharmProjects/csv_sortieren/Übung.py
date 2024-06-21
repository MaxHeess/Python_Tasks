age = int(input("Bitte gebe dein Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer ist jünger als 18")
elif age == 18:
    print("Der Nutzer ist exakt 18")
elif age == 30:
    print("Der Nutzer ist exakt 30")
else:
    print("Der Nutzer ist volljährig")

print("Programmende")