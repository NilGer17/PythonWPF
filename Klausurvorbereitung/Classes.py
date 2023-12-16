import numpy as np
from matplotlib import pyplot as plt
class Verarbeiten:
    input = []  # Eingangsvariable für die Daten
    stuetzstellen: list  # Liste für die Stützstellen
    function_values: list  # Liste für die Funktionswerte
    
    def __init__(self, input) -> None:
        """
        Konstruktor der Klasse.

        :param input: Eingangsdaten, die verarbeitet werden sollen.
        """
        self.input = input  # Speichert die Eingabedaten
        self.get_stuetzstellen()  # Ruft die Methode zur Extraktion der Stützstellen auf
        self.get_function_values()  # Ruft die Methode zur Extraktion der Funktionswerte auf

    def get_stuetzstellen(self):
        """
        Extrahiert die Stützstellen aus den Eingabedaten.

        :return: Liste der Stützstellen.
        """
        self.stuetzstellen = np.transpose(self.input)[0]  # Extrahiert die erste Spalte (Stützstellen)
        return self.stuetzstellen  # Gibt die Stützstellen zurück

    def print_stuetzstellen(self):
        """
        Gibt die Stützstellen aus.
        """
        print(self.stuetzstellen) 

    def get_function_values(self):
        """
        Extrahiert die Funktionswerte aus den Eingabedaten.

        :return: Liste der Funktionswerte.
        """
        self.function_values = np.transpose(self.input)[1:]  # Extrahiert die restlichen Spalten (Funktionswerte)
        return self.function_values  # Gibt die Funktionswerte zurück

    def print_function_values(self):
        """
        Gibt die Funktionswerte aus.
        """
        for f in self.function_values:
            print(f)

    def find_all_crossings(self):
        """
        Findet alle Schnittpunkte zwischen den Funktionen.

        :return: Liste von Schnittpunkten.
        """
        returnlist = []
        for fxs in range(0, len(self.function_values)):
           returnlist.append(self.find_Schnittpunkt(self.function_values[fxs-1], self.function_values[fxs], self.stuetzstellen))
        return returnlist  # Gibt eine Liste von Schnittpunkten zurück

    def find_Schnittpunkt(self, fx1, fx2, s):
        """
        Findet die Schnittpunkte zwischen zwei Funktionen an den Stützstellen.

        :param fx1: Funktionswerte der ersten Funktion.
        :param fx2: Funktionswerte der zweiten Funktion.
        :param s: Stützstellen.

        :return: Liste von Tupeln mit Stützstellen und Funktionswerten an den Schnittpunkten.
        """
        SchnittList = []  # Liste für die Funktionswerte an den Schnittpunkten
        StList = []  # Liste für die Stützstellen an den Schnittpunkten

        for i in range(0, len(fx1), 1):
            # Durchläuft die Werte der Funktionen
            if(fx1[i-1] > fx2[i-1] and fx1[i] <= fx2[i]):
                # Prüft auf Schnittpunkte zwischen den Funktionen
                SchnittList.append(fx1[i])
                StList.append(s[i])
            if(fx1[i-1] < fx2[i-1] and fx1[i] >= fx2[i]):
                SchnittList.append(fx1[i])
                StList.append(s[i])
        
        return list(zip(StList, SchnittList))  # Kombiniert Stützstellen und Funktionswerte zu Tupeln und gibt eine Liste der Schnittpunkte zurück
    def find_max(self, fx1, s):
        listofmaximas = []
        listofstuet = []
        for i in range(2, len(fx1), 1):
            if (fx1[i-2] < fx1[i-1] and fx1[i-1] > fx1[i]):
                listofmaximas.append(fx1[i-1])
                listofstuet.append(s[i-1])
        return list(zip(listofstuet, listofmaximas))
    def find_all_maxima(self):
        returnlist = []
        for fxs in range(0, len(self.function_values)):
           returnlist.append(self.find_max(self.function_values[fxs], self.stuetzstellen))
        return returnlist  # Gibt eine Liste von Schnittpunkten zurück