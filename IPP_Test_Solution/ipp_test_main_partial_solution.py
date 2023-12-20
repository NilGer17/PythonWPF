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

Abgabe:
- Erstellen Sie eine zip-Datei ihres Python-Moduls und der 'ipp_marker.txt'-Datei.
- Der Name der zip-Datei lautet: ipp_test_nachname_vorname.zip.
- Laden Sie die zip-Datei in den Abgabeordner in Stud.iP hoch.
================================================================================
"""

#---------------------------------------
# Importierte Module
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------
# Globale Variablen
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ACHTUNG: Die Pfadnamen der Dateien sind anzupassen!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#---------------------------------------
# Name der Eingabedatei mit Trackdaten: Format s. Datei
# Pfad zur Eingabedatei auf meinem Linux
#input_filename = '/home/holtv/ipp_track.txt'
#-------------------
# Pfad zur Eingabedatei, wenn diese im gleichen Verzeichnis liegt, in dem auch das 
# Python-Skript gestartet wird.
input_filename = './ipp_track.txt'
#---------------------------------------

#---------------------------------------
# Name der Ausgabedatei für Marker-Daten
#-------------------
# Pfad zur Ausgabedatei auf meinem Linux
#output_filename = '/home/holtv/ipp_marker.txt'
#-------------------
# Pfad zur Ausgabedatei, wenn diese im gleichen Verzeichnis liegt, in dem auch das 
# Python-Skript gestartet wird.
output_filename = './ipp_marker.txt'
#---------------------------------------

# Marker-Intervall-Distanz
marker_dist = 50.0
#---------------------------------------
input_filename = '/home/nils/PhythonWPF/IPP_Test_Solution/ipp_track.txt'

# Name der Ausgabedatei für Marker-Daten
output_filename = '/home/nils/PhythonWPF/IPP_Test_Solution/ipp_marker.txt'

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
def read_data_01(filename):
  data = np.loadtxt(filename) 
  return data
#---------------------------------------
def main_01():
  # Einlesen der Daten
  data = read_data_01(input_filename)

  # Ausgabe der Anzahl der Datensätze
  print('Anzahl Datensätze:', data.shape[0])
  # Ausgabe der Anzahl der Daten
  print(data)

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
def read_data_02(filename):
  data = np.loadtxt(filename) 
  return data
#---------------------------------------
def plot_track_02(x, y):
  fig, ax = plt.subplots()
  ax.plot(x, y,'b')
  ax.set_aspect('equal')
  ax.grid()
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  plt.show()
#---------------------------------------
def main_02():
  # Einlesen der Daten
  data = read_data_02(input_filename)

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]

  # Ausgabe des Tracks als x/y-Plot
  plot_track_02(x, y)

"""
================================================================================
Aufgabe 03

1. Einlesen der Daten wie in Aufgabe 01
2. Ausgabe der Trackdaten als x/y-Plot wie in Aufgabe 02
3. Jeden 10. Wegpunkt des Tracks durch ein rotes X im Plot markieren
================================================================================
"""
def read_data_03(filename):
  data = np.loadtxt(filename) 
  return data
#---------------------------------------
def plot_track_03(x, y):
  fig, ax = plt.subplots()
  ax.plot(x, y,'b')
  ax.plot(x[::10], y[::10],'rx')
  ax.set_aspect('equal')
  ax.grid()
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  plt.show()
#---------------------------------------
def main_03():
  # Einlesen der Daten
  data = read_data_03(input_filename)

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_03(x, y)

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
def read_data_04(filename):
  data = np.loadtxt(filename) 
  return data
#---------------------------------------
def ev_marker_04(x, y, marker_dist):
  xm = []
  ym = []
  dist = 0.0
  for i in range(1,x.shape[0]):
    i_dist = np.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    dist += i_dist
    if dist >= marker_dist:
      xm.append(x[i])
      ym.append(y[i])
      dist = 0.0

  return xm, ym
#---------------------------------------
def plot_track_04(x, y, xm, ym):
  fig, ax = plt.subplots()
  ax.plot(x, y,'b')
  ax.plot(xm, ym,'rx')
  ax.set_aspect('equal')
  ax.grid()
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  plt.show()
#---------------------------------------
def main_04():
  # Einlesen der Daten
  data = read_data_04(input_filename)

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]

  # Berechnung der Weg-Marker im Abstand >= marker_dist
  xm, ym = ev_marker_04(x,y,marker_dist)

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_04(x, y, xm, ym)

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
def read_data_05(filename):
  data = np.loadtxt(filename) 
  return data
#---------------------------------------
def ev_marker_05(x, y, marker_dist):
  xm = []
  ym = []
  dist = 0.0
  for i in range(1,x.shape[0]):
    i_dist = np.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)

    if dist + i_dist >= marker_dist:
      rel_dist = (marker_dist-dist)/i_dist
      rel_vec = [x[i]-x[i-1],y[i]-y[i-1]]
      mp_x = x[i-1] + rel_dist*rel_vec[0]
      mp_y = y[i-1] + rel_dist*rel_vec[1]

      xm.append(mp_x)
      ym.append(mp_y)
      dist = (1.0-rel_dist) * i_dist
      #print(i_dist, rel_dist)
    else:
      dist += i_dist

  return xm, ym
#-------------------------------------
def write_marker_05(xm,ym,filename):
  np.savetxt(filename,np.transpose([xm,ym]))
#-------------------------------------
def plot_track_05(x,y,xm,ym):
  fig, ax = plt.subplots()
  ax.plot(x, y,'b')
  ax.plot(xm, ym,'rx')
  ax.set_aspect('equal')
  ax.grid()
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  plt.show()
#---------------------------------------
def main_05():
  # Einlesen der Daten
  data = read_data_05(input_filename)

  t = data[:,0]
  x = data[:,1]
  y = data[:,2]

  # Berechnung der Weg-Marker im Abstand >= marker_dist
  xm, ym = ev_marker_05(x,y,marker_dist)

  # Speichern der Weg-Marker in Datei
  write_marker_05(xm,ym,output_filename)

  # Ausgabe des Tracks als x/y-Plot mit Weg-Markern
  plot_track_05(x,y,xm,ym)
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
class track_data_t_06():
  def __init__(self):
    pass
  #-------------------------------------
  def read_data(self, filename):
    self.data = np.loadtxt(filename) 
    self.t = self.data[:,0]
    self.x = self.data[:,1]
    self.y = self.data[:,2]
  #-------------------------------------
  def ev_marker(self, marker_dist):
    self.xm = []
    self.ym = []
    dist = 0.0
    for i in range(1,self.x.shape[0]):
      i_dist = np.sqrt((self.x[i]-self.x[i-1])**2+(self.y[i]-self.y[i-1])**2)

      if dist + i_dist >= marker_dist:
        rel_dist = (marker_dist-dist)/i_dist
        rel_vec = [self.x[i]-self.x[i-1],self.y[i]-self.y[i-1]]
        mp_x = self.x[i-1] + rel_dist*rel_vec[0]
        mp_y = self.y[i-1] + rel_dist*rel_vec[1]

        self.xm.append(mp_x)
        self.ym.append(mp_y)
        dist = (1.0-rel_dist) * i_dist
        #print(i_dist, rel_dist)
      else:
        dist += i_dist
  #-------------------------------------
  def write_marker(self,file_name):
    np.savetxt(file_name,np.transpose([self.xm,self.ym]))
  #-------------------------------------
  def plot_track(self):
    self.fig, self.ax = plt.subplots()
    self.ax.plot(self.x, self.y,'b')
    self.ax.plot(self.xm, self.ym,'rx')
    self.ax.set_aspect('equal')
    self.ax.grid()
    self.ax.set_xlabel('x')
    self.ax.set_ylabel('y')
    plt.show()
#---------------------------------------
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
class track_data_t_07():
  def __init__(self):
    pass
  #-------------------------------------
  def read_data(self, filename):
    self.data = np.loadtxt(filename) 
    self.t = self.data[:,0]
    self.x = self.data[:,1]
    self.y = self.data[:,2]
  #-------------------------------------
  def ev_marker(self, marker_dist):
    self.xm = []
    self.ym = []
    dist = 0.0
    for i in range(1,self.x.shape[0]):
      i_dist = np.sqrt((self.x[i]-self.x[i-1])**2+(self.y[i]-self.y[i-1])**2)

      if dist + i_dist >= marker_dist:
        rel_dist = (marker_dist-dist)/i_dist
        rel_vec = [self.x[i]-self.x[i-1],self.y[i]-self.y[i-1]]
        mp_x = self.x[i-1] + rel_dist*rel_vec[0]
        mp_y = self.y[i-1] + rel_dist*rel_vec[1]

        self.xm.append(mp_x)
        self.ym.append(mp_y)
        dist = (1.0-rel_dist) * i_dist
        #print(i_dist, rel_dist)
      else:
        dist += i_dist
  #-------------------------------------
  def write_marker(self,file_name):
    np.savetxt(file_name,np.transpose([self.xm,self.ym]))
  #-------------------------------------
  def plot_track(self):
    self.fig, self.ax = plt.subplots()
    self.ax.plot(self.x, self.y,'b')
    self.ax.plot(self.xm, self.ym,'rx')
    self.ax.set_aspect('equal')
    self.ax.grid()
    self.ax.set_xlabel('x')
    self.ax.set_ylabel('y')
    plt.show()
  #-------------------------------------
  def plot_data(self):
    #TODO
    pass
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

"""
================================================================================
Hauptprogramm

Die aufzurufende bzw. zu bearbeitende Teilaufgabe ist jeweils einzukommentieren.
================================================================================
"""
if __name__ == '__main__':
  print('IPP Test')

  
  #main_01()
  #main_02()
  #main_03()
  #main_04()
 # main_05()
 # main_06()
  main_07()

  exit()
#-------------------------------------------------------------------------------
