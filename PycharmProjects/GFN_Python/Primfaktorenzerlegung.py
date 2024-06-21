def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors
def main():

    try:
        number = int(input("Geben Sie eine Zahl ein: "))

        if number <= 0:
            print("Bitte geben Sie eine positive Zahl größer als 0 ein.")
        else:
            factors = prime_factors(number)
            print(f"Die Primfaktorenzerlegung von {number} ist: {' * '.join(map(str, factors))}")
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein.")

if __name__ == "__main__":
    antwort = "j"  # Antwortvariable für Menü-Steuerung
    while antwort == "j":  # Schleife für Wiederholung
        main()
        antwort = input("Noch einmal? (j)")  # Abfrage für die Wiederholung