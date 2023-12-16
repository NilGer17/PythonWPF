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
# ---NEU---BEGIN
import etmain
# ---NEU---END

#-------------------------------------------------------------------------------
# Klasse zur Repräsentation des simulierten Fahrzeugs
class sim_vehicle_t:
  #-------------------------------------
  # Konstruktor
  def __init__(self):
    self.T = 0.1  # Abtastzeit [s]

    """ Formparameter/Abmessungen des Fahrzeugs """
    # Länge [m]
    self.L  = 5.0 #10.0 # cfg['L'] #4.0
    # Breite [m]
    self.B  = 2.0 #5.0 # cfg['B'] #2.0
    # 1/2 Länge [m]
    self.L2 = self.L/2 
    # 1/2 Breite [m]
    self.B2 = self.B/2
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

    #-------------------------------
    # Definieren der Punkte zur geometrischen Darstellung des Fahrzeugs
    self.v_p_o_h = np.empty((4,3), dtype=np.float32)
    self.v_p_w_h = np.empty((4,3), dtype=np.float32)
    self.v_p_w_n = self.v_p_w_h[:,:2] # Referenz auf die [x,y]-Spalten von v_p_w_h

    # Homogene Transformationsmatrizen Objekt->Welt
    self.htm_o2w = np.empty((3,3), dtype=np.float32)

    self.evHtm()
    self.update_p_o()
    self.update_p_w()
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

    # Darstellung anhand der neuen Lage berechnen und anzeigen
    self.evHtm()
    self.update_p_o()
    self.update_p_w()
  #------------------------------------- 

  # Die folgenden Methoden dienen der Berechnung der Grafikelemente zur
  # Darstellung des Fahrzeugs und der Transformation im Darstellungsbereich
  #------------------------------------- 
  # Berechnung der Homogenen Transformationsnmatrix HTM O->W
  def evHtm(self):
    # Berechnung einiger Hilfsgrößen
    ca = cos(self.psi_i1)
    sa = sin(self.psi_i1)
    tx = self.x_i1
    ty = self.y_i1
    #-------------------------------------
    self.htm_o2w[:,:] = [[ca, -sa, tx], [sa, ca, ty], [0, 0, 1]]
  #------------------------------------- 
  # Berechnung der Merkmale in Objektkoordinaten
  def update_p_o(self):
    self.v_p_o_h[:,:] = [[+self.L2,+self.B2,1],[-self.L2,+self.B2,1],
                         [-self.L2,-self.B2,1],[+self.L2,-self.B2,1]]
  #------------------------------------- 
  # Transformation der Merkmale in Weltkoordinaten
  def update_p_w(self):
    for i_p in range (0, 4):
      self.v_p_w_h[i_p,:] = np.matmul(self.htm_o2w, self.v_p_o_h[i_p,:])
  #------------------------------------- 
  def init_draw(self, ax):
    self.v_patch = plt.Polygon(self.v_p_w_n, closed=True, animated=False)
    self.v_patch.set_fill(True)
    self.v_patch.set_edgecolor('b')
    self.v_patch.set_linewidth(1)
    ax.add_patch(self.v_patch)

    self.update_draw(ax)
  #------------------------------------- 
  def set_animated(self, animated):
    self.v_patch.set_animated(animated)
  #------------------------------------- 
  def update_draw(self, ax):
    self.v_patch.set_xy(self.v_p_w_n)
    ax.draw_artist(self.v_patch)
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
    self.AA = 2.5   # Radstand in [m]

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
    """ # ---ALT---BEGIN
    self.fig, self.ax = plt.subplots()
    self.fig.set_size_inches(self.fig_width, self.fig_height)
    self.fig.set_tight_layout(True)
    """ # ---ALT---END

    # ---NEU---BEGIN
    self.fig, self.ax = etmain.load_track([90, -65, pi/2, 0])
    # ---NEU---END

    #---------------------------------------
    # Schrittweises Berechnen UND Plotten
    #---------------------------------------
    self.dt_pause = 0.05   # für dT läuft die Animation in "Echtzeit", für < dT schneller, für > dT langsamer

    self.i = 0
    self.t = 0.0

    # ---NEU---BEGIN
    self.xy_line, = self.ax.plot(self.x[:self.i], self.y[:self.i],'b:')
    # ---NEU---END
    self.ax.axis('equal')
    self.ax.set_xlim(-100,+100)
    self.ax.set_ylim(-100,+100)
    self.ax.set_xlabel('x [m]')
    self.ax.set_ylabel('y [m]')

    plt.pause(self.dt_pause)

    # ---NEU---BEGIN
    self.sim_vehicle.init_draw(self.ax)
    # ---NEU---END

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
    # ---NEU---BEGIN
    self.sim_vehicle.update_draw(self.ax)
    # ---NEU---END
 
    #""" #NEU

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
    """ # ---ALT---BEGIN
    self.xy_line.set_data(self.x[:self.i],self.y[:self.i])
    """ # ---ALT---END

    #""" # ---NEU---BEGIN
    i_start = max(self.i-100,0)
    self.xy_line.set_data(self.x[i_start:self.i],self.y[i_start:self.i])
    #""" # ---NEU---END

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

