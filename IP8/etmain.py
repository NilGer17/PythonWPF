#!/usr/bin/env python  
## @package EgoTrack
"""
EGOTRACK:
2D-Simulation einer Autofahrt auf einem Rundkurs.
Die Kurse werden in Form von Tabellen angelegt und zu Beginnn eingelesen.
Die Grundidee der Kursdefinition ist, dass ein "Markierungs"-Fahrzeug einen
definierten Kurs mit einer konstanten Geschwindigkeit abfährt und man sich
in festen Abtastschritten die Stützpunkte des Kurses in Tabellenform merkt.
Aus dem so erzeugten Kurs werden dann später die Markierungen des Kurses 
generiert und für die Anzeige aufbereitet.

Für den Anwendungsfall muss dann ein Fahrzeug auf dem Kurs positioniert werden.
Das Fahrzeug kann sich im Prinzip gesteuert oder geregelt frei auf dem Kurs bewegen.
Um dem Kurs folgen zu können, muss die Relativlage des Fahrzeugs zum Kurs bestimmt werden.
Diese Bestimmung kann unter Nutzung der Kursdaten, d.h. der Stützpunkte entlang des Kurses,
erfolgen. Sie ist aber nicht ganz trivial und in dieser Version noch nicht enthalten.
Stattdessen wird das Fahrzeug zu Demozwecken einfach entlang der bekannten Stützpunkte 
über den Kurs "geschoben".
(Anmerkung: Die Bestimmung der Relativlage ist in der MATLAB-Version aber enthalten, nur noch nicht 
nach Python portiert.)
"""
#--------------------------------------------------------------------import roslib
import sys
#import rospy

import math
import numpy as np
import time


import time
import numpy as np
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as lines
#---------------------------------
#import etconfig as cfg
import etconfig as cfg

#from ego_track.utils import *

from simtrack import sim_track_t


def GoDriving():
  vis_mpl = False

  # Kurs einlesen und Stützpunkte generieren
  simTrack = sim_track_t(cfg.simTrack['Kursname'])
  [xh, xr, xl, xm, xtr, xtl, xnt, segment] = simTrack.getTrack()
  #------------------------------------------------------
  # Zeichenfenster anlegen
  plt.ion()
  #plt.ioff()

  with plt.style.context('dark_background'):
    fig, ax = createFigTrack()
    
  # Kurs darstellen
  #[m_xl, m_xm, m_xr] = plotTrack(ax, xh, xr, xl, xm, xtr, xtl, segment)
  [m_xl, m_xr] = plotTrack(ax, xh, xr, xl, xm, xtr, xtl, segment)
  plt.show(block = False)
  plt.pause(0.01)

  plt.show()

  while True:
    plt.pause(0.01)


def load_track(start_position):

  # Kurs einlesen und Stützpunkte generieren
  simTrack = sim_track_t(cfg.simTrack['Kursname'],start_position)
  [xh, xr, xl, xm, xtr, xtl, xnt, segment] = simTrack.getTrack()
  #------------------------------------------------------
  # Zeichenfenster anlegen
  plt.ion()
  #plt.ioff()

  with plt.style.context('dark_background'):
    fig, ax = createFigTrack()
    
  # Kurs darstellen
  #[m_xl, m_xm, m_xr] = plotTrack(ax, xh, xr, xl, xm, xtr, xtl, segment)
  [m_xl, m_xr] = plotTrack(ax, xh, xr, xl, xm, xtr, xtl, segment)

  return fig,ax


###########################################################################################

###########################################################################################

#--------------------------------------------------------------------
# Anlegen des Zeichenfensters mit diversen Einstellungen für die
# Ausgabe
#--------------------------------------------------------------------
def createFigTrack():

  # Breite und Höhe des Zeichenfensters in Inch 
  WIDTH_SIZE  = cfg.figTrack['width']
  HEIGHT_SIZE = cfg.figTrack['height']

  # Anlegen des Plots und der Achsen
  fig, ax = plt.subplots()

  #ax.scatter()

  # Größe setzen
  fig.set_size_inches(WIDTH_SIZE, HEIGHT_SIZE)

  # Hintergrundfarbe des Fensters setzen
  fig.patch.set_facecolor((0,0,0))

  # Rand schmal halten
  fig.set_tight_layout(True)

  # Hintergrundfarbe des eigentlichen Plots setzen
  ax.set_facecolor((0,0,0))

  # Achsen identisch skalieren
  ax.set_aspect('equal')

  # Ränder beschneiden
  ax.margins(x=0.01, y=0.01)

  # keine Achsenskalierung anzeigen
  ax.set_xticks(ticks=[])
  ax.set_yticks(ticks=[])

  # das wars...
  return fig, ax


#--------------------------------------------------------------------
# Darstellung des Kurses mit allen Markierungen
#--------------------------------------------------------------------
def plotTrack(ax, xh, xr, xl, xm, xtr, xtl, Segment):

  # Arrays für Markierungen anlegen 
  m_xl = np.zeros(len(xh),dtype=np.uint8)
  m_xm = np.zeros(len(xh),dtype=np.uint8)
  m_xr = np.zeros(len(xh),dtype=np.uint8)

  #------------------------------------------------------------------------
  # Rechte Markierung
  #------------------------------------------------------------------------
  # Ganz einfache Variante: Komplette Linie 
  # ax.plot(xr[:,0], xr[:,1],'w')
  #------------------------------------------------------------------------
  # Linie mit Unterbechungen nach Segmentvorgaben
  for i_s in range(len(Segment)):
    if (Segment[i_s].Mark.R == 1):
      plxr = ax.plot(xr[Segment[i_s].i_s:Segment[i_s].i_e,0], 
                     xr[Segment[i_s].i_s:Segment[i_s].i_e,1], 'w', lw=2)
      m_xr[Segment[i_s].i_s:Segment[i_s].i_e] = 1
  #------------------------------------------------------------------------
  # Linke Markierung
  #------------------------------------------------------------------------
  # Ganz einfache Variante: Komplette Linie 
  # ax.plot(xl[:,0], xl[:,1],'w')
  #------------------------------------------------------------------------
  # Linie mit Unterbechungen nach Segmentvorgaben
  for i_s in range(len(Segment)):
    if (Segment[i_s].Mark.L == 1):
      ax.plot(xl[Segment[i_s].i_s:Segment[i_s].i_e,0], 
              xl[Segment[i_s].i_s:Segment[i_s].i_e,1], 'w', lw=2)
      m_xl[Segment[i_s].i_s:Segment[i_s].i_e] = 1
  #------------------------------------------------------------------------
  # Mittlere Markierung
  #------------------------------------------------------------------------
  # Ganz einfache Variante: Komplette gestrichelte Linie 
  # ax.plot(xh[:,0], xh[:,1],'w--')
  #------------------------------------------------------------------------
  # Einfache Variante: Gestrichelte Linie nach Segmentvorgaben
  # for i_s in range(len(Segment)):
  #  if (Segment[i_s].Mark.M == 1):
  #    ax.plot(xh[Segment[i_s].i_s:Segment[i_s].i_e,0], 
  #            xh[Segment[i_s].i_s:Segment[i_s].i_e,1], 'w--', lw=2)
  #------------------------------------------------------------------------
  # Realistischere Variante: 
  # Die Mittellinie wird aus vielen Linien aufgebaut, die jeweils der Länge
  # realer Mittelmarkierungen entsprechen. Leider ein ziemlicher Aufwand 
  # sowohl beim Zeichnen als auch hinsichtlich der Laufzeit, weil mit steigender
  # Zahl an Linien die Laufzeit zunimmt.
  """
  xdm = np.zeros(len(xh), dtype=np.uint8)

  for i_s in range(len(Segment)):
    if (Segment[i_s].Mark.M == 1):
      for i_n in range(Segment[i_s].i_s, Segment[i_s].i_e):
        xdm[i_n] = 1

  ds = 0
  LineOn = True
  i_a = np.argmax(xdm > 0)
  i_e = len(xdm)
  for i_n in range(i_a, i_e):
    ds = ds + xh[i_n, 3]
    if LineOn:
      if xdm[i_n] == 0 or ds > 2:
        LineOn = False
        ds = 0
        ax.plot(xh[i_a:i_n-1, 0], 
                xh[i_a:i_n-1, 1], 'w-', lw=2)
        m_xm[i_a:i_n-1] = 1
    else:
      if ds > 2 and xdm[i_n] == 1:
        LineOn = True
        ds = 0 
        i_a = i_n
      else:
        xdm[i_n] = 0

  return m_xl, m_xm, m_xr
  """
  return m_xl, m_xr
#------------------------------------------------------------------------
# Hauptprogramm: Einstiegspunkt
if __name__ == '__main__':

  #-------------------------------------
  # Variante A ohne ROS
  GoDriving()
  #simTrack = sim_track_t(cfg.simTrack['Kursname'])

  #GoDrivingROS(cfg.simTrack['Kursname'])
  #-------------------------------------
#-----------------------------------------------------------------------

