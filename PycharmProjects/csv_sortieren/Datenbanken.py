import sqlite3
import os.path
from sqlite3 import Connection


def personentabelle_anlegen():
    try:
        is_db_open = False
        if os.path.exists("personenverwaltung.db"):
            connection: Connection = sqlite3.connect("personenverwaltung.db")
            is_db_open = True
            cursor = connection.cursor()
            sql_anweisung = "CREATE TABLE IF NOT EXISTS Person( " \
                            "PersonID INTEGER PRIMARY KEY AUTOINCREMENT, " \
                            "Name TEXT, " \
                            "Vorname TEXT, " \
                            "Groesse REAL, " \
                            "Gewicht REAL, " \
                            "Geburtsdatum DATE, " \
                            "OrtID INTEGER " \
                            ")"
            cursor.execute(sql_anweisung)
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        if is_db_open == True:
            connection.close()

def person_hinzufuegen():
    try:
        is_db_open = False
        if os.path.exists("personenverwaltung.db"):
            connection = sqlite3.connect("personenverwaltung.db")
            is_db_open = True
        cursor = connection.cursor()
        sql_anweisung = ("INSERT INTO Person(Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID) "
                         + "VALUES('Braumann','Kurt',1.86,76.00,'1998-04-03',1)")

        cursor.execute(sql_anweisung)
        connection.commit()
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])
    finally:
        if is_db_open == True:
            connection.close()

def personendaten_anzeigen():
    try:
        is_db_open = False
        if os.path.exists("personenverwaltung.db"):
            connection = sqlite3.connect("personenverwaltung.db")
            is_db_open = True
        cursor = connection.cursor()
        sql_anweisung = "SELECT * FROM Person"
        cursor.execute(sql_anweisung)
        for datensatz in cursor:
            print(str(datensatz[0]) + " " +  # PersonID
                  str(datensatz[1]) + " " +  # Name
                  str(datensatz[2]) + " " +  # Vorname
                  str(datensatz[3]) + " " +  # Groesse
                  str(datensatz[4]) + " " +  # Gewicht
                  str(datensatz[5]) + " " +  # Geburtsdatum
                  str(datensatz[6]) + "\n")  # OrtID
    except Exception as e:
        print("Es ist folgender Fehler aufgetreten: \n" + e.args[0])

personentabelle_anlegen()
person_hinzufuegen()
personendaten_anzeigen()