#!/usr/bin/python3
"""
IPP - Ingenieurwissenschaftliches Programmieren mit Python
Aufgabe A-8.1.1 

- Einlesen Lambda und v von Tastatur oder Joystick
- Trennung der fahrzeugbezogenen Funktionalität in eine separate Klasse

- Unvollständige Implementationsvorlage

(c) Prof. Dr.-Ing. Volker von Holt / Fahrzeuginformatik
"""
# Importieren der notwendigen Module
import numpy as np
import matplotlib.pyplot as plt
from math import *

# ACHTUNG: Hier den tatsächlich verwendeten Modulnamen eintragen!
import kb_listener

#-------------------------------------------------------------------------------
# Klasse zur Repräsentation des simulierten Fahrzeugs
class sim_vehicle_t:
  #-------------------------------------
  # Konstruktor
  def __init__(self):
    self.T = 0.1  # Abtastzeit [s]

    # Achsabstand [m]
    self.AA = 2.5 # cfg['AA'] #2.5  

    self.v_soll = 0.0
    self.Lambda_soll = 0.0

    # Wir führen für x,y, psi jeweils 2 Variablen ein:
    # x_i:  x zum i.ten Zeitschritt (dem aktuellen)
    # x_i1: x zum (i+1).ten Zeitschritt (dem folgenden)
    self.x_i = self.x_i1 = 0.0
    self.y_i = self.y_i1 = 0.0
    self.psi_i = self.psi_i1 = 0.0
  #------------------------------------- 
  # Setzen von v_soll
  def set_v_soll(self,v_soll):
    self.v_soll = v_soll
  #------------------------------------- 
  # Setzen von Lambda_soll
  def set_Lambda_soll(self,Lambda_soll):
    self.Lambda_soll = Lambda_soll
  #------------------------------------- 
  # Bewegung um einen Zeitschritt T
  def move(self):
    # Werte des letzten Zyklus => "alte" Werte für den aktuellen Durchlauf  
    self.x_i = self.x_i1
    self.y_i = self.y_i1
    self.psi_i = self.psi_i1

    # Berechnung für den folgenden Zeitschritt i+1 aus i
    self.x_i1 = self.x_i + self.T * self.v_soll * np.cos(self.psi_i)
    self.y_i1 = self.y_i + self.T * self.v_soll * np.sin(self.psi_i)
    self.psi_i1 = self.psi_i + self.T * self.v_soll * np.tan(self.Lambda_soll/self.AA)

    self.x_i1 = max(min(self.x_i1,+100),-100)
    self.y_i1 = max(min(self.y_i1,+100),-100)
  #------------------------------------- 


#-------------------------------------------------------------------------------
# Klasse zur Darstellung der Simulationsumgebung 
class drive_sim_t:
  #------------------------------------- 
  def __init__(self):
    #---------------------------------------
    # Initialisierungen
    #---------------------------------------
    # Abtastzeit
    self.T = 0.1

    self.sim_vehicle = sim_vehicle_t()

    # Festlegen der Größe des Zeichenfensters
    self.fig_width = 10
    self.fig_height = 10

    self.fig_closed = False

    #---------------------------------------
    # Anlegen der Datenstrukturen
    #---------------------------------------
    # Jetzt noch die NumPy-Arrays für die Position in (ebenen) Weltkoordinaten (x,y,psi)
    self.x = np.zeros(100, dtype=np.float32)
    self.y = np.zeros(100, dtype=np.float32)
    self.psi = np.zeros(100, dtype=np.float32)

    #---------------------------------------
    # Jetzt erfolgt die grafische Ausgabe
    #---------------------------------------
    self.fig, self.ax = plt.subplots()
    self.fig.set_size_inches(self.fig_width, self.fig_height)
    self.fig.set_tight_layout(True)

    #---------------------------------------
    # Schrittweises Berechnen UND Plotten
    #---------------------------------------
    self.dt_pause = 0.05   # für dT läuft die Animation in "Echtzeit", für < dT schneller, für > dT langsamer

    self.i = 0
    self.t = 0.0

    self.xy_line, = self.ax.plot(self.x[:self.i], self.y[:self.i])
    self.ax.axis('equal')
    self.ax.set_xlim(-100,+100)
    self.ax.set_ylim(-100,+100)
    self.ax.set_xlabel('x [m]')
    self.ax.set_ylabel('y [m]')

    plt.pause(self.dt_pause)

    self.fig.canvas.mpl_connect('close_event', self.on_close)

  def on_close(self, event):
      self.fig_closed = True

  #------------------------------------- 
  def run(self,v,Lambda):
    self.sim_vehicle.set_v_soll(v)
    self.sim_vehicle.set_Lambda_soll(Lambda)

    # Berechnung für den folgenden Zeitschritt i+1 aus i
    self.sim_vehicle.move()

    # Wir merken uns die neuen Werte in den zugehörigen Feldern (fürs Plotten)
    if self.i+1 >= self.x.shape[0]:
      self.x = np.resize(self.x,self.x.shape[0]+100)
      self.y = np.resize(self.y,self.y.shape[0]+100)
      self.psi = np.resize(self.psi,self.psi.shape[0]+100)

    self.x[self.i+1] = self.sim_vehicle.x_i1
    self.y[self.i+1] = self.sim_vehicle.y_i1
    self.psi[self.i+1] = self.sim_vehicle.psi_i1

    # Zeit und Index weiterzählen
    self.i += 1
    self.t += self.T

    # Plot aktualisieren
    self.xy_line.set_data(self.x[:self.i],self.y[:self.i])

    # jetzt den Plot aktualisieren und die MPL-Eventschleife bedienen
    plt.gcf().canvas.draw_idle()
    plt.gcf().canvas.start_event_loop(0.001)

    return self.fig_closed

#---------------------------------------------
# Hauptprogramm: Einstiegspunkt
if __name__ == '__main__':

  T = 0.1
  t = 0.0
  terminated = False

  drive_sim = drive_sim_t()

  # Jetzt müssen wir noch den Keyboard-Listener anlegen und starten
  kb_listener = kb_listener.kb_listener_t()
  kb_listener.start_listening()

  while not terminated:
    # Einlesen des aktuellen Werts von Lambda und v vom kb_listener
    print('t=%5.1f   v=%4.1f   Lambda=% 4.2f' % (t,kb_listener.vehicle_ctrl.v,kb_listener.vehicle_ctrl.Lambda))  
    terminated = drive_sim.run(kb_listener.vehicle_ctrl.v,kb_listener.vehicle_ctrl.Lambda) or kb_listener.terminate
    t = t + T

#---------------------------------------------

