import sqlite3
import os

name = input("Wie ist dein Nachname? ")
vorname = input("Wie ist dein Vorname? ")
gebdatum = input("Gib dein Geburtsdatum im Format YYYY-MM-DD ein, z.B. 2003-10-27: ")


def erstelle_tabelle():
    try:
        dbconnection = sqlite3.connect('test.db')
        cursor = dbconnection.cursor()

        sql_anweisung = """CREATE TABLE IF NOT EXISTS Person(
                            Name TEXT,
                            Vorname TEXT,
                            Geburtsdatum DATE
                            )"""
        cursor.execute(sql_anweisung)
        dbconnection.commit()
    except Exception as e:
        print(f"Es ist folgender Fehler aufgetreten: \n{e}")
    finally:
        dbconnection.close()


def person_hinzufuegen(name, vorname, gebdatum):
    try:
        if os.path.exists("test.db"):
            connection = sqlite3.connect("test.db")
            cursor = connection.cursor()
            sql_anweisung = "INSERT INTO Person(Name, Vorname, Geburtsdatum) VALUES (?, ?, ?)"
            cursor.execute(sql_anweisung, (name, vorname, gebdatum))
            connection.commit()
    except Exception as e:
        print(f"Es ist folgender Fehler aufgetreten: \n{e}")
    finally:
        connection.close()


# Tabelle erstellen
erstelle_tabelle()

# Person hinzufügen
person_hinzufuegen(name, vorname, gebdatum)

print("Die Daten wurden hinzugefügt")