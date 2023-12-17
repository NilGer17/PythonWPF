#!/usr/bin/python3
"""
IPP - Ingenieurwissenschaftliches Programmieren mit Python

Prüfungs-Testlauf

(c) Prof. Dr.-Ing. Volker von Holt / Fahrzeuginformatik
"""
"""
================================================================================
Allgemeine Hinweise:

- Der Test ist in 7 aufeinander aufbauende Teilaufgaben gegliedert.
- Jede Teilaufgabe ist unabhängig von den anderen Teilaufgaben zu implementieren
  und für sich eigenständig ablauffähig.
- Die Teilaufgaben und eventuell dazu gehörige Funktionen und/oder Klassen werden
  durch einen Namenssuffix '_0x' (x = Nummer der Teilaufgabe) gekennzeichnet.
  (Das hat zur Folge, dass wiederholt genutzte Funktionen ggf. mehrfach kopiert
  und umbenannt werden müssen.)
- Der Aufruf der einzelnen Teilaufgaben erfolgt im "Hauptprogramm" (am Ende der
  Datei) durch entsprechende Auskommentierung von jeweils EINER Teilaufgabe.
================================================================================
"""

#---------------------------------------
# Importierte Module
#---------------------------------------


import numpy as np

from matplotlib import pyplot as plt
#---------------------------------------
# Globale Variablen
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ACHTUNG: Die Pfadnamen der Dateien sind anzupassen!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#---------------------------------------
# Name der Eingabedatei mit Trackdaten: Format s. Datei
input_filename = '/home/nils/PhythonWPF/IPP_Test/ipp_track.txt'

# Name der Ausgabedatei für Marker-Daten
output_filename = '/home/nils/PhythonWPF/IPP_Test/ipp_marker.txt'

# Marker-Intervall-Distanz
marker_dist = 50.0

"""
================================================================================
Aufgabe 01

1. Einlesen der Datei 'input_filename' mit Anzahl der eingelesenen Datensätze
   und Ausgabe der Werte
   - Entwerfen Sie für das eigentliche Einlesen der Daten eine Funktion, die den
     Dateinamen als Argument erhält und die eingelesenen Daten als Rückgabewert
     liefert.
================================================================================
"""
#---------------------------------------
# Hier Funktion read_data_01() definieren
def read_data_01(file):
  return np.loadtxt(file, skiprows=1, unpack=1)
#---------------------------------------
def main_01():
  # Einlesen der Daten
  input_data = read_data_01(input_filename)

  # Ausgabe der Anzahl der Datensätze
  print(len(input_data))

  # Ausgabe der Anzahl der Daten
  print(input_data)
#---------------------------------------

"""
================================================================================
Aufgabe 02

1. Einlesen der Daten wie in Aufgabe 01
2. Ausgabe der Trackdaten als x/y-Plot mittels der Matplotlib in der Form:
   - blaue, durchgezogenen Linie
   - Aspektverhältnis (x:y = 1:1)
   - Anzeige eines Grids
   - Achsenbeschriftungen
   Erstellen Sie hierzu eine Funktion 'plot_track()' entsprechend der in
   'main' gegebenen Signatur.
================================================================================
"""
#---------------------------------------
# Hier Funktion read_data_02() definieren
def read_data_02(file):
  return np.loadtxt(file, skiprows=1, unpack=1)
#---------------------------------------
# Hier Funktion plot_track_02() definieren
#---------------------------------------
def plot_track_02(x, y):
  plt.plot(x, y, "blue")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid(1)  
  plt.gca().set_aspect("equal") #Aspektverhältnis gleich
  plt.show()

def main_02():
  # Einlesen der Daten
 input_data = read_data_02(input_filename)


  # Ausgabe des Tracks als x/y-Plot
 a =  plot_track_02(input_data[1],input_data[2])
#---------------------------------------

"""
================================================================================
Aufgabe 03
1. Einlesen der Daten wie in Aufgabe 01
2. Ausgabe der Trackdaten als x/y-Plot wie in Aufgabe 02
3. Jeden 10. Wegpunkt des Tracks durch ein rotes X im Plot markieren
================================================================================
"""
#---------------------------------------
# Hier Funktion read_data_03() definieren
def read_data_03(file):
  return np.loadtxt(file, skiprows=1, unpack=1)
#---------------------------------------
# Hier Funktion plot_track_03() definieren
#---------------------------------------
def plot_track_03(x, y):
  plt.plot(x, y, "blue")
  #print(range(0,len(x), 10))
  for i in range(0,len(x), 10):
    print(i)
    plt.scatter(x[i], y[i], marker="X",c="red" )
  #plt.scatter(x[::10], y[::10], marker="X",c="red" ) #andere Option zum Plotten
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid(1)  
  plt.show()

def main_03():
  # Einlesen der Daten
  input_data = read_data_03(input_filename)
  x = input_data[1]
  y = input_data[2]

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_03(x, y)
#---------------------------------------

"""
================================================================================
Aufgabe 04

1. Einlesen der Daten wie in Aufgabe 01
2. Ausgabe der Trackdaten als x/y-Plot wie in Aufgabe 02
3. Jetzt soll nicht einfach jeder 10. Wegpunkt markiert werden, sondern die 
   Marker sollen immer nach Überschreiten einer vorgegebenen Distanz 
   'marker_dist' zum vorhergehenden Marker gesetzt werden. Dazu müssen die 
   Entfernungen der Marker aufsummiert werden. Die Entfernung zwischen 2
   aufeinanderfolgenden Trackpositionen erhält man aus der euklidischen Distanz
   (Pythagoras d = sqrt(dx**2 + dy**2)).
   Erstellen Sie für die Bestimmung der Markerpositionen eine Funktion
   'ev_marker()' entsprechend der in 'main()' gegebenen Signatur.
4. Übergeben Sie die ermittelten Marker-Positionen als zusätzliche Argumente
   an die Plot-Funktion und stellen Sie die Marker als rotes X im x/y-Plot dar.
================================================================================
"""
import math
#---------------------------------------
# Hier Funktion read_data_04() definieren
def read_data_04(file):
  return np.loadtxt(file, skiprows=1, unpack=1)
#---------------------------------------
# Hier Funktion ev_marker_04() definieren
def ev_marker_04(x, y, marker_dist):
  dx = 0
  dy =  0
  xm = []
  ym = []
  xm.append(x[0])
  ym.append(y[0])
  for i in range(0,len(x)):
    distance = math.sqrt(dx**2 + dy**2)
    if  distance >= marker_dist:
      xm.append(x[i])
      ym.append(y[i])
      dx = 0
      dy = 0
    dx = x[i] - xm[-1] 
    dy = y[i] - ym[-1] 
  
  return xm, ym
#---------------------------------------
# Hier Funktion plot_track_04() definieren
#---------------------------------------
def plot_track_04(x, y, xm, ym):
  plt.plot(x, y, "blue")
  #print(range(0,len(x), 10))
  plt.scatter(xm, ym, marker="X",c="red" )
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid(1)  
  plt.show()
def main_04():
  # Einlesen der Daten
  input_data = read_data_04(input_filename)
  x = input_data[1]
  y = input_data[2]


  # Berechnung der Weg-Marker im Abstand >= marker_dist
  #xm, ym = ev_marker_04(x,y,10)
  xm, ym = ev_marker_04(x,y,marker_dist)
  #print(xm)
  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_04(x, y, xm, ym)
#---------------------------------------


#Pause 16:50 -> 1h

#Start 9:00


"""
================================================================================
Aufgabe 05

1. Einlesen der Daten wie in Aufgabe 01
2. Ausgabe der Trackdaten als x/y-Plot wie in Aufgabe 02
3. In Aufgabe 04 wurden die Marker immer nach Überschreiten des vorgegebenen
   Abstands 'marker_dist' gesetzt. Dadurch entspricht der Marker-Abstand i.d.R. 
   nicht exakt der 'marker_dist'. Um den vorgegebenen Abstand exakt zu treffen,
   d.h. die Marker wirklich stets im Abstand 'marker_dist' zu setzen, müssen
   wir zwischen den letzten beiden Punkten eines Segments interpolieren, also
   zwischen dem letzten Wegpunkt der < 'marker_dist' war und dem ersten 
   Wegpunkt der > 'marker_dist' ist. 
   Ändern Sie die Funktion 'ev_marker()' so ab, dass die exakte Markerposition
   durch (lineare) Interpolation berechnet wird.
4. Speichern Sie die ermittelten Marker-Positionen in der Datei 'output_filename'
   ab. Erstellen Sie hierzu eine Funktion 'write_marker()' entsprechend der in
   'main()' gegebenen Signatur. Das Ausgabeformat soll einen Datensatz pro Zeile 
   enthalten.
5. Übergeben Sie die ermittelten Marker-Positionen als zusätzliche Argumente
   an die Plot-Funktion und stellen Sie die Marker als rotes X im x/y-Plot dar.
================================================================================
"""
#---------------------------------------
# Hier Funktion read_data_05() definieren
def read_data_05(file):
  return np.loadtxt(file, skiprows=1, unpack=1)
#---------------------------------------
# Hier Funktion ev_marker_05() definieren
def ev_marker_05(x, y, marker_dist):
  dx = 0
  dy =  0
  xm = []
  ym = []
  xm.append(x[0])
  ym.append(y[0])
 # print(x, np.interp(marker_dist, x, y, period=marker_dist) )
  for i in range(0,len(x)):
    #print(x, np.interp(10, x, y) )
    distance = math.sqrt(dx**2 + dy**2)
    if  distance >= marker_dist:
      anteil = marker_dist/distance #Anteil, wie weit vom letzten marker gegangen werden muss um genau MarkerDist zu erreichen
      print(anteil)
      x_interp = xm[-1] + (dx*anteil) #letzter marker + abstand zum nächsten der mindestens 50 weg ist * anteil
      y_interp = ym[-1] + (dy*anteil)
      xm.append(x_interp)
      ym.append(y_interp)
      dx = 0
      dy = 0
    dx = x[i]- xm[-1] 
    dy = y[i]- ym[-1]   
  return xm, ym
#---------------------------------------
# Hier Funktion write_marker_05() definieren
def write_marker_05(xm, ym, output_filename):
  out = list(zip(xm,ym))
  header = "%15s\t%15s"%("x","y")
  np.savetxt(output_filename, out, header=header)
#---------------------------------------
# Hier Funktion plot_track_05() definieren
def plot_track_05(x, y, xm, ym):
  plt.plot(x, y, "blue")
  #print(range(0,len(x), 10))
  plt.scatter(xm, ym, marker="X",c="red" )
  plt.xlabel("x")
  plt.ylabel("y")
  plt.grid(1)  
  plt.show()
#---------------------------------------

def main_05():
  # Einlesen der Daten
  input_data = read_data_04(input_filename)
  x = input_data[1]
  y = input_data[2]


  # Berechnung der Weg-Marker im Abstand >= marker_dist
  xm, ym = ev_marker_05(x,y,marker_dist)

  # Speichern der Weg-Marker in Datei
  write_marker_05(xm,ym,output_filename)

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_05(x, y, xm, ym)
#---------------------------------------

"""
================================================================================
Aufgabe 06

In dieser Aufgabe geht es darum, unsere Problemstellung objektorientiert zu
formulieren (so etwas nennt man auch "Refactoring"). 
Hierzu soll:
1. Eine Klasse 'track_data_t' erstellt werden.
2. Diese soll über Methoden verfügen, die unsere bisher erarbeitete Funktionalität
   abbildet:
  - Einlesen der Daten
    read_data(input_filename)
  - Berechnung der Weg-Marker im Abstand >= marker_dist
    ev_marker(marker_dist)
  - Speichern der Weg-Marker in Datei
    write_marker(output_filename)
  - Ausgabe des Tracks als x/y-Plot mit Weg-Markern
    plot_track()
3. Die gesamten Datenelemente sollen nun als Attribute in der Klasse angelegt
   werden, so dass sich die 'main()'-Funktion auf das Aufrufen der Methoden 
   beschränkt ohne Daten weiterzureichen wie u.a.

(Anmerkung: Falls Sie die Aufgaben 5 und/oder 4 nicht erfolgreich bearbeiten 
konnten, können Sie diese Aufgabe im Wesentlichen auch auf Basis der Aufgabe 3 
erstellen.)
================================================================================
"""
#---------------------------------------
# Hier Klasse track_data_t definieren
#---------------------------------------
class track_data_t_06:
  x:list
  y:list
  xm:list
  ym:list
  def __init__(self) -> None:
    self.x = []
    self.xm =[]
    self.y = []
    self.ym = []
  def read_data(self,input_filename):
    input = np.loadtxt(input_filename, skiprows=1, unpack=1)
    self.x = input[1]
    self.y = input[2]
  def ev_marker(self, marker_dist):
    dx = 0
    dy =  0
    self.xm.append(self.x[0])
    self.ym.append(self.y[0])
    for i in range(0,len(self.x)):
      distance = math.sqrt(dx**2 + dy**2)
      if  distance >= marker_dist:
        anteil = marker_dist/distance #Anteil, wie weit vom letzten marker gegangen werden muss um genau MarkerDist zu erreichen
        x_interp = self.xm[-1] + (dx*anteil) #letzter marker + abstand zum nächsten der mindestens 50 weg ist * anteil
        y_interp = self.ym[-1] + (dy*anteil)
        self.xm.append(x_interp)
        self.ym.append(y_interp)
        dx = 0
        dy = 0
      dx = self.x[i]- self.xm[-1] 
      dy = self.y[i]- self.ym[-1] 
  def write_marker(self,output_filename):
    out = list(zip(self.xm,self.ym))
    header = "%15s\t%15s"%("x","y")
    np.savetxt(output_filename, out, header=header)
  def plot_track(self):
    plt.plot(self.x, self.y, "blue")
    plt.scatter(self.xm, self.ym, marker="X",c="red" )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(1)  
    plt.show()

def main_06():
  # Instanziieren eines Objekts der Klasse 'track_data_t'
  track_data = track_data_t_06()

  # Einlesen der Daten
  track_data.read_data(input_filename)

  # Berechnung der Weg-Marker im Abstand >= marker_dist
  track_data.ev_marker(marker_dist)

  # Speichern der Weg-Marker in Datei
  track_data.write_marker(output_filename)

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  track_data.plot_track()
#---------------------------------------

"""
================================================================================
Aufgabe 07

Ergänzen Sie die in Aufgabe 06 erstellte Klasse 'track_data_t' um eine Methode
'plot_data()' zur Darstellung der x/y-Positionen als Funktion der Zeit t:
- Das Diagramm soll über 2 Subplots übereinander verfügen.
- Im 1.(oberen) Subplot: x = f(t) in blau, gestrichelt
- Im 2.(unteren) Subplot: y = f(t) in rot, gepunktet

================================================================================
"""
class track_data_t_07:
  t:list
  x:list
  y:list
  xm:list
  ym:list
  def __init__(self) -> None:
    self.x = []
    self.xm =[]
    self.y = []
    self.ym = []
    self.t = []
  def read_data(self,input_filename):
    input = np.loadtxt(input_filename, skiprows=1, unpack=1)
    self.x = input[1]
    self.y = input[2]
    self.t = input[0]
  def ev_marker(self, marker_dist):
    dx = 0
    dy =  0
    self.xm.append(self.x[0])
    self.ym.append(self.y[0])
    for i in range(0,len(self.x)):
      distance = math.sqrt(dx**2 + dy**2)
      if  distance >= marker_dist:
        anteil = marker_dist/distance #Anteil, wie weit vom letzten marker gegangen werden muss um genau MarkerDist zu erreichen
        x_interp = self.xm[-1] + (dx*anteil) #letzter marker + abstand zum nächsten der mindestens 50 weg ist * anteil
        y_interp = self.ym[-1] + (dy*anteil)
        self.xm.append(x_interp)
        self.ym.append(y_interp)
        dx = 0
        dy = 0
      dx = self.x[i]- self.xm[-1] 
      dy = self.y[i]- self.ym[-1] 
  def write_marker(self,output_filename):
    out = list(zip(self.xm,self.ym))
    header = "%15s\t%15s"%("x","y")
    np.savetxt(output_filename, out, header=header)
  def plot_track(self):
    plt.figure("Track")
    plt.plot(self.x, self.y, "blue")
    plt.scatter(self.xm, self.ym, marker="X",c="red" )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(1)  
    #plt.show()
  def plot_data(self):
    fig, ax = plt.subplots(2)
    fig.suptitle("Data")
    ax[0].plot(self.t, self.x, "blue", "--")
    ax[0].set_xlabel("t")
    ax[0].set_ylabel("x")
    ax[1].plot(self.t, self.y, "red", ".") 
    ax[1].set_xlabel("t")
    ax[1].set_ylabel("y")

    plt.show()
#---------------------------------------
# Hier Klasse track_data_t definieren
#---------------------------------------
def main_07():
  # Instanziieren eines Objekts der Klasse 'track_data_t'
  track_data = track_data_t_07()

  # Einlesen der Daten
  track_data.read_data(input_filename)

  # Berechnung der Weg-Marker im Abstand >= marker_dist
  track_data.ev_marker(marker_dist)

  # Speichern der Weg-Marker in Datei
  track_data.write_marker(output_filename)

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  track_data.plot_track()

  # Ausgabe der x- und y-Position als Funktion der Zeit t
  track_data.plot_data()
#---------------------------------------


#11:00 ->2h 

"""
================================================================================
Hauptprogramm

Die aufzurufende bzw. zu bearbeitende Teilaufgabe ist jeweils einzukommentieren.
================================================================================
"""
if __name__ == '__main__':
  print('IPP Test')

  #main_01()
 # main_02()
  main_03()
  #main_04()
  #main_05()
  #main_06()
 # main_07()

  exit()
#-------------------------------------------------------------------------------
