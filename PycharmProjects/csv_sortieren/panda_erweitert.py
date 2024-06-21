import pandas as pd

# CSV-Datei einlesen
data = pd.read_csv("aufgabe50.csv")

# Daten nach Nachnamen sortieren
sorted_data = data.sort_values(by=["last_name"], ascending=True)

# Anfangsbuchstaben der Nachnamen zählen
letter_counts = sorted_data["last_name"].str[0].value_counts().sort_index()

# Die sortierten Daten in eine neue CSV-Datei schreiben
sorted_data.to_csv("aufgabe_sortiert.csv", index=False)

# Die Zählungen der Anfangsbuchstaben der Nachnamen als DataFrame erstellen
letter_counts_df = pd.DataFrame({"initial": letter_counts.index, "count": letter_counts.values})

# Anhängen der Zählungen an die sortierten Daten und in die neue CSV-Datei schreiben
with open("aufgabe_sortiert.csv", "a") as f:
    f.write('\n')
    letter_counts_df.to_csv(f, index=False)