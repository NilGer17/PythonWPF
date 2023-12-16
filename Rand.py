import random

# Liste von Vor- und Nachnamen
vorname = ["Max", "Anna", "Lena", "Tim", "Sophie", "Felix", "Laura", "Simon", "Sebastian", "Tom", "Tim"]
nachname = ["Schmidt", "Müller", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Mayer","Hut", "Strumpfhose", "Springer"]

# Anzahl der Einträge im Dokument
anzahl_einträge = 20

# Öffnen einer Datei zum Schreiben
with open('zufallsdaten.txt', 'w') as file:
    for _ in range(anzahl_einträge):
        # Zufällige Auswahl von Vor- und Nachnamen
        zufälliger_vorname = random.choice(vorname)
        zufälliger_nachname = random.choice(nachname)
        
        # Zufälliger Float-Wert zwischen 1,4 und 5
        zufälliger_float = round(random.uniform(1.4, 5), 2)
        
        # Schreiben der Daten in die Datei
        file.write(f"{zufälliger_vorname} {zufälliger_nachname} {zufälliger_float}\n")
