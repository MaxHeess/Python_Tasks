daten = []
input_datei = open("Log-Datei.txt","r")

zeile = input_datei.readline()

while zeile:
    daten.append(zeile)
    zeile = input_datei.readline()

input_datei.close()

status = ""
hosts = []
host = ""

for i in range(len(daten)):
    satz = daten[i].split('"')
    status = (satz[2].split(" "))[1]

    if status == "404":
        host = (satz[0].split('-'))[0]
        hosts.append(host)
print(hosts)

