#!/usr/bin/python3

#---------------------------------------
# Importierte Module
#---------------------------------------
# TODO ...
import numpy as np
from matplotlib import pyplot as plt
#---------------------------------------
# Globale Variablen
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ACHTUNG: Die Pfadnamen der Dateien sind anzupassen!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#---------------------------------------
# Eingabedateien mit Trackdaten: Format s. Datei
#-------------------
# Pfad zu den Eingabedateien auf meinem Linux
#input_filename_1 = '/home/holtv/ipp_rp3a.txt'
#input_filename_2 = '/home/holtv/ipp_rp3b.txt'
#-------------------
# Pfad zu den Eingabedateien, wenn diese im gleichen Verzeichnis liegen, in dem auch das 
# Python-Skript gestartet wird.
input_filename_1 = '/home/nils/PhythonWPF/IPP_RP/ipp_rp3a.txt'
input_filename_2 = '/home/nils/PhythonWPF/IPP_RP/ipp_rp3b.txt'
#---------------------------------------

# Marker-Intervall-Distanz
marker_dist = 50.0
#---------------------------------------


"""
================================================================================
Aufgabe 01

1. Einlesen der Datei 'input_filename_1' mit Anzahl der eingelesenen Datensätze
   und Ausgabe der Werte
   - Entwerfen Sie für das eigentliche Einlesen der Daten eine Funktion, die den
     Dateinamen als Argument erhält und die eingelesenen Daten als Rückgabewert
     liefert.
================================================================================
"""
#---------------------------------------
def read_data_01(filename):
  return np.loadtxt(filename)
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def main_01():
  # Einlesen der Daten
  data = read_data_01(input_filename_1)
  # Ausgabe der Anzahl der Datensätze
  print(data.shape[0])
  # Ausgabe der Anzahl der Daten
  print(np.transpose(data))
  pass  # Platzhalter - kann nach Implementierung entfernt werden
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
def read_data_02(filename):
  return np.loadtxt(filename)
#---------------------------------------
def plot_track_02(x, y):
  plt.plot(x,y, "blue")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.gca().set_aspect("equal")
  plt.grid(1)
  plt.show()
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def main_02():
  # Einlesen der Daten
  data = read_data_01(input_filename_1)
  # Ausgabe des Tracks als x/y-Plot
  t, x, y = np.transpose(data)
  plot_track_02(x, y)
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------


"""
================================================================================
Aufgabe 03

1. Die Funktion zum Einlesen der Daten soll nun erweitert werden um die 
   Möglichkeit, direkt nach dem Einlesen einen optionalen Offset auf die 
   Positionsdaten x/y zu geben. 
   Für die Track-Daten aus 'input_filename_1' soll der Offset aber (0,0) 
   betragen.
2. Die Plotfunktion soll dergestalt modifiziert werden, dass jeder 10. Wegpunkt
   des Tracks durch ein rotes X im Plot markiert wird.
================================================================================
"""
#---------------------------------------
def read_data_03(filename, x_offset=0, y_offset=0):
  t, x, y = np.loadtxt(filename, unpack=1)
  return x+x_offset, y+y_offset
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def plot_track_03(x, y):
  plt.plot(x,y, "blue")
  for i in range(0,len(x), 10):
    plt.scatter(x[i], y[i], marker="x",c="red" )
  plt.xlabel("x")
  plt.ylabel("y")
  plt.gca().set_aspect("equal")
  plt.grid(1)
  plt.show()
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def main_03():
  # Einlesen der Daten
  # Testen Sie den x/y-Offset mit verschiedenen Werten (ungleich 0) durch!
  x,y = read_data_03(input_filename_1, 10, 50)
  # Ausgabe des Tracks als x/y-Plot
  plot_track_03(x,y)
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------


"""
================================================================================
Aufgabe 04

1. Einlesen der Daten wie in Aufgabe 03
2. Im Hinblick auf die weiteren Aufgaben soll 'plot_track()' nun etwas 
   modifiziert werden, um universeller anwendbar zu sein:
   - Die Erzeugung des Plots selber soll vor dem Aufruf von 'plot_track()' in 
     'main()' erfolgen.
   - 'plot_track()' muss dann zum Plotten die Achsen ('ax') als Argument 
     erhalten.
   - Zusätzlich soll der Plot-Stil (z.B. 'b-') sowohl für den Track selber,
     wie für die Wegpunkte variabel sein und als weiteres  Argument an 
     'plot_track()' übergeben werden.
   - Die weiteren Einstellungen für den Plot wie das Aspektverhältnis,
     das Grid etc. sollen nach 'plot_track()' wieder in 'main()' erfolgen.
   - Anmerkung: 'plot_track()' wird dann sehr kurz und knapp!
   Erstellen Sie hierzu eine Funktion 'plot_track()' entsprechend der in
   'main' gegebenen Signatur.
================================================================================
"""
#---------------------------------------
def read_data_04(filename, x_offset=0, y_offset=0):
  t, x, y = np.loadtxt(filename, unpack=1)
  return x+x_offset, y+y_offset
#---------------------------------------
def plot_track_04(ax, x, y, track_style, marker_style):
  ax.plot(x,y, track_style)
  for i in range(0,len(x), 10):
    ax.scatter(x[i], y[i], marker="x",c=marker_style )
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def main_04():
  # Einlesen der Daten
  x,y=read_data_04(input_filename_1, 0, 0)
  #--- Beginn der Plotbefehle
  # Erzeugen des Plots
  fig, axs = plt.subplots()
  # Ausgabe des Tracks als x/y-Plot
  plot_track_04(axs, x, y, 'b--', 'red')
  # Jetzt noch die weiteren Einstellungen für den Plot vornehmen ...
  axs.set_aspect("equal")
  axs.set_xlabel("x")
  axs.set_ylabel("y")
  plt.grid(1)
  # ... und den Plot anzeigen
  plt.show()
  #--- Ende der Plotbefehle

  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------


"""
================================================================================
Aufgabe 05

In dieser Aufgabe geht es darum, unsere Problemstellung objektorientiert zu
formulieren (so etwas nennt man auch "Refactoring"). 
Hierzu soll:
1. Eine Klasse 'track_data_t' erstellt werden.
2. Diese soll über Methoden verfügen, die unsere bisher erarbeitete Funktionalität
   abbildet:
  - Einlesen der Daten
    read_data(input_filename, x_offset, y_offset)
  - Ausgabe des Tracks als x/y-Plot mit Weg-Markern
    plot_track()
3. Die gesamten Datenelemente sollen nun als Attribute in der Klasse angelegt
   werden, so dass sich die 'main()'-Funktion auf das Aufrufen der Methoden 
   beschränkt ohne Daten weiterzureichen wie u.a.
================================================================================
"""
#---------------------------------------
class track_data_t_05():
  x:list
  y:list
  t:list
  def __init__(self):
    pass  # Platzhalter - kann nach Implementierung entfernt werden
  #-------------------------------------
  def read_data(self, filename, x_off=0, y_off=0):
    t_Tem, x_Tem, y_Tem = np.loadtxt(filename, unpack=1)
    self.t = t_Tem
    self.x = x_Tem+x_off
    self.y = y_Tem+y_off
    pass  # Platzhalter - kann nach Implementierung entfernt werden
  #-------------------------------------
  def plot_track(self, ax, track_style, marker_style):
    ax.plot(self.x,self.y, track_style)
    for i in range(0,len(self.x), 10):
      ax.scatter(self.x[i], self.y[i], marker="x",c=marker_style )
    pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------
def main_05():
  track = track_data_t_05()
  # Einlesen der Daten
  track.read_data(input_filename_1, 0, 0)
  #--- Beginn der Plotbefehle ---
  fig, ax = plt.subplots()
  # Ausgabe des Tracks als x/y-Plot
  track.plot_track(ax, "b--", "red")
  # Jetzt noch die weiteren Einstellungen für den Plot vornehmen ...
  ax.set_aspect("equal")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  plt.grid(1)
  plt.show()
  pass  # Platzhalter - kann nach Implementierung entfernt werden
#---------------------------------------


"""
================================================================================
Aufgabe 06

Ergänzen Sie die in Aufgabe 06 erstellte Klasse 'track_data_t' um eine Methode
'plot_data()' zur Darstellung der x- bzw. y-Positionen als Funktion der Zeit t:
- Das Diagramm soll über 2 Subplots übereinander verfügen.
- Im 1.(oberen) Subplot: x = f(t) in blau, gestrichelt
- Im 2.(unteren) Subplot: y = f(t) in blau, gestrichelt
- Anmerkung: Auch bei 'plot_data()' soll der Plot-Stil für die beiden Kurven
  als Parameter übergeben werden.
================================================================================
"""
#---------------------------------------
class track_data_t_06():
  x:list
  y:list
  t:list
  def __init__(self):
    pass 
  #-------------------------------------
  def read_data(self, filename, x_off=0, y_off=0):
     t_Tem, x_Tem, y_Tem = np.loadtxt(filename, unpack=1)
     self.t = t_Tem
     self.x = x_Tem+x_off
     self.y = y_Tem+y_off
     pass  
  #-------------------------------------
  def plot_track(self, ax, track_style, marker_style):
    ax.plot(self.x,self.y, track_style)
    for i in range(0,len(self.x), 10):
      ax.scatter(self.x[i], self.y[i], marker="x",c=marker_style )
  #-------------------------------------
  def plot_data(self, ax, x_style, y_style):
    ax[0].plot(self.t, self.x, x_style)
    ax[1].plot(self.t, self.y, y_style)
#---------------------------------------
def main_06():
  # Instanziieren eines Objekts der Klasse 'track_data_t'
  # TODO ... track_data = ...
  track = track_data_t_06()
  # Einlesen der Daten
  # TODO ... track_data.read_data()
  track.read_data(input_filename_1, 0, 0)
  #--- Beginn der Plotbefehle für den Track ---
  fig, ax = plt.subplots(1)
  track.plot_track(ax, "b--", "red")
  ax.set_aspect("equal")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  plt.grid(1)
  plt.show()
  #--- Ende der Plotbefehle für den Track ---
  #--- Beginn der Plotbefehle für die Daten ---
  fig, ax = plt.subplots(2)
  track.plot_data(ax, "b--", "b--")
  ax[0].set_xlabel("t")
  ax[0].set_ylabel("x")
  ax[1].set_xlabel("t")
  ax[1].set_ylabel("y")
  ax[0].grid(1)
  ax[1].grid(1)
  plt.show()
#---------------------------------------


"""
================================================================================
Aufgabe 07

In dieser Aufgabe wollen wir jetzt die Vorteile unserer Umsetzung als Klasse
nutzen. Wir wollen nun 2 (unterschiedliche) Dateien mit Trackdaten einlesen:
- Legen Sie 2 Objekte der Klasse 'track_data' an.
- Laden Sie die Trackdaten aus 'input_filename_1' bzw. 'input_filename_2'.
  Der 2. Track soll mit einem Offset von x_offset=-72.5 und y_offset=+5.0 
  geladen werden.
- Stellen Sie beide Tracks als x/y-Plot in EINEM Diagramm dar:
  - Track 1: blau, durchgezogene Linie, Marker als rotes x.
  - Track 2: schwarz, durchgezogene Linie, Marker als rotes x.
- Stellen Sie Zeitverläufe von x und y für beide Tracks in EINEM Diagramm  
  mit 2 Plots für x bzw. y dar:
  - Track 1: x bzw. y in: blau, gestrichelt
  - Track2 : x bzw. y in: rot, gepunktet
Anmerkung: Im Idealfall müssen Sie lediglich 4 Zeilen (für den 1. Track) ändern 
           und 4 weitere (für den 2. Track) ergänzen!
================================================================================
"""
#---------------------------------------
class track_data_t_07():
  x:list
  y:list
  t:list
  def __init__(self):
    pass 
  #-------------------------------------
  def read_data(self, filename, x_off=0, y_off=0):
     t_Tem, x_Tem, y_Tem = np.loadtxt(filename, unpack=1)
     self.t = t_Tem
     self.x = x_Tem+x_off
     self.y = y_Tem+y_off
  #-------------------------------------
  def plot_track(self, ax, track_style, marker_style):
    ax.plot(self.x,self.y, track_style)
    for i in range(0,len(self.x), 10):
      ax.scatter(self.x[i], self.y[i], marker="x",c=marker_style )
  #-------------------------------------
  def plot_data(self, ax, x_style, y_style):
    ax[0].plot(self.t, self.x, x_style)
    ax[1].plot(self.t, self.y, y_style)
#---------------------------------------
def main_07():
  # TODO ...
  track1 = track_data_t_07()
  track2 = track_data_t_07()
  track1.read_data(input_filename_1, 0, 0)
  track2.read_data(input_filename_2, -72.5, +5)
  #ein gemeinsamer Subplot für beide Tracks
  fig, ax = plt.subplots()
  track1.plot_track(ax, "blue", "red")
  track2.plot_track(ax, "black", "red")
  ax.set_aspect("equal")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  plt.grid(1)
  plt.show()
  #2 Subplots für die beiden Tracks/Daten erzeugen
  fig, ax = plt.subplots(2)
  track1.plot_data(ax, "b--", "b--")
  track2.plot_data(ax, "r", "r")
  ax[0].set_title("Track1")
  ax[1].set_title("Track2")
  ax[0].grid(1)
  ax[1].grid(1)
  plt.show()
#---------------------------------------


"""
================================================================================
Aufgabe 08

Erweitern Sie die Klasse 'track_data_t' um eine Methode 'ev_arg()', die für 
jedes Tracksegment den Kurswinkel berechnet und in einer Liste speichert.
Der Kurswinkel ergibt sich zu: arg = atan2( dy, dx) (hier: np.atan2())

Erweitern Sie das Plotten der Daten und die Methode 'plot_data()' so, dass  
der Kurswinkel in einem 3. Plot für beide Tracks dargestellt wird.
================================================================================
"""
#---------------------------------------
class track_data_t_08():
  x:list
  y:list
  t:list
  arg:list
  def __init__(self):
    self.arg = []
  #-------------------------------------
  def read_data(self, filename, x_off=0, y_off=0):
    t_Tem, x_Tem, y_Tem = np.loadtxt(filename, unpack=1)
    #Offests addieren und in Membervariable abspeichern
    self.t = t_Tem
    self.x = x_Tem+x_off
    self.y = y_Tem+y_off
  #-------------------------------------
  def ev_arg(self):
    #um am anfang direkt die Runde zum letzten Element zu bekommen
    for i in range(0,len(self.x)):
      dx = self.x[i] - self.x[i-1]
      dy = self.y[i] - self.y[i-1]
      self.arg.append(np.arctan2(dx, dy))
  #-------------------------------------
  def plot_track(self, ax, track_style, marker_style):
    ax.plot(self.x,self.y, track_style)
    for i in range(0,len(self.x), 10):
      ax.scatter(self.x[i], self.y[i], marker="x",c=marker_style )
  #-------------------------------------
  def plot_data(self, ax, x_style, y_style, arg_style):
    #Plotten der Daten in die 3 Subplots
    ax[0].plot(self.t, self.x, x_style)
    ax[1].plot(self.t, self.y, y_style)
    ax[2].plot(self.t, self.arg, arg_style)
#---------------------------------------
def main_08():
    track1 = track_data_t_08()
    track2 = track_data_t_08()
  # Berechnen des Kurswinkels
    track1.read_data(input_filename_1, 0, 0)
    track2.read_data(input_filename_2, -72.5, +5)
  #--- Beginn der Plotbefehle ---
    fig, ax = plt.subplots()
    track1.plot_track(ax, "blue", "red")
    track2.plot_track(ax, "black", "red")
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.grid(1)
    plt.show()
    #3 Subplots für Track1, Track2, und Winkel
    fig, ax = plt.subplots(3)
    track1.ev_arg()
    track2.ev_arg()
    track1.plot_data(ax, "b--", "b--", "green")
    track2.plot_data(ax, "r", "r", "yellow")
    ax[0].grid(1)
    ax[1].grid(1)
    ax[2].grid(1)
    plt.show()
#---------------------------------------


"""
================================================================================
Hauptprogramm

Die aufzurufende bzw. zu bearbeitende Teilaufgabe ist jeweils einzukommentieren.
================================================================================
"""
if __name__ == '__main__':
  print('IPP Rechner-Prüfung')

  #main_01()
  #main_02()
  #main_03()
  #main_04()
  #main_05()
  #main_06()
  #main_07()
  main_08()

  exit()
#-------------------------------------------------------------------------------
