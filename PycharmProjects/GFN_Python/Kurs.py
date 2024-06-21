input_datei = open("KURS_EIN.txt","r")
output_datei = open("KURS_DM.txt","w")

Euro_to_DM = 1.95583
zeile = input_datei.readline()

while zeile:
    satz = zeile.split(",")
    wkn = satz[0]
    kurs_euro = float(satz[1])
    kurs_dm = kurs_euro * Euro_to_DM

    formatted_kurs_dm = "{: .2f}".format(kurs_dm).replace(".", ",")
    output_datei.write(f"WKN={wkn} WERT={formatted_kurs_dm} DM\n")
    zeile = input_datei.readline()

input_datei.close()
output_datei.close()