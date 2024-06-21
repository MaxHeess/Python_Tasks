import csv

# Einlesen der CSV-Datei
input_file = "aufgabe50.csv"
data = []

with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Erste Zeile als Header
    for row in reader:
        data.append(row)

# Sortieren der Daten nach Nachnamen
data.sort(key=lambda x: x[1])  # x[1] ist der Nachname

# Initialisieren von Variablen für die Zählung
sorted_data = []
current_letter = ''
count_by_letter = {}
total_count = 0

# Daten verarbeiten und sortieren
for row in data:
    last_name = row[1]
    first_letter = last_name[0].upper()
    if first_letter != current_letter:
        if current_letter != '':
            sorted_data.append([f'Summe {current_letter}:', count_by_letter[current_letter]])
        current_letter = first_letter
        count_by_letter[current_letter] = 0
    count_by_letter[current_letter] += 1
    sorted_data.append(row)
    total_count += 1

# Letzte Summenzeile hinzufügen
if current_letter != '':
    sorted_data.append([f'Summe {current_letter}:', count_by_letter[current_letter]])

# Gesamtsumme hinzufügen
sorted_data.append(['Gesamtsumme:', total_count])

# Ergebnisse in eine neue CSV-Datei schreiben
output_file = 'sorted_output.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)  # Header schreiben
    writer.writerows(sorted_data)

print(f'Die sortierte und ausgewertete Liste wurde in {output_file} geschrieben.')