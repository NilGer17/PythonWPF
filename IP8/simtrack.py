## @package DriveSim2D
"""
Enthält die Klassen für das Einlesen der Kurstabellen und das 
Generieren der für die Simulation notwendigen Track-Informationen.
"""

#--------------------------------------------------------------------

import numpy as np
from math import *

#---------------------------------------

import kurstabellen as kt
from kurstabellen  import * 
from kurstabellen import *

#from ego_track.kurstabellen import Kurs_CC_2015_6_MIRROR_TrackTable
#import  ego_track.kurstabellen as kt

#--------------------------------------------------------------------
#
# Hilfsklasse zur Speicherung der Markierungsarten eines
# Kurssegments.
#
class track_marker_t:
  MARK_M    = int(1)
  MARK_L    = int(2)
  MARK_R    = int(4)
  MARK_SLRA = int(8)
  MARK_SLRE = int(16)
  MARK_SLLA = int(32)
  MARK_SLLE = int(64)
  MARK_P    = int(128)

  M    = 0  #   1
  L    = 0  #   2
  R    = 0  #   4
  SLRA = 0  #   8
  SLRE = 0  #  16
  SLLA = 0  #  32
  SLLE = 0  #  64
  P    = 0  # 128

  def __init__(self):
    pass

  def clear(self):
    self.M    = 0  #   1
    self.L    = 0  #   2
    self.R    = 0  #   4
    self.SLRA = 0  #   8
    self.SLRE = 0  #  16
    self.SLLA = 0  #  32
    self.SLLE = 0  #  64
    self.P    = 0  # 128

  def setMarkBF(self, MarkBF):
    if (MarkBF >= self.MARK_P):
      self.P = 1
      MarkBF = MarkBF - self.MARK_P
    if (MarkBF >= self.MARK_SLLE):
      self.SLLE = 1
      MarkBF = MarkBF - self.MARK_SLLE
    if (MarkBF >= self.MARK_SLLA):
      self.SLLA = 1
      MarkBF = MarkBF - self.MARK_SLLA
    if (MarkBF >= self.MARK_SLRE):
      self.SLLE = 1
      MarkBF = MarkBF - self.MARK_SLRE
    if (MarkBF >= self.MARK_SLRA):
      self.SLRA = 1
      MarkBF = MarkBF - self.MARK_SLRA
    if (MarkBF >= self.MARK_R):
      self.R = 1
      MarkBF = MarkBF - self.MARK_R
    if (MarkBF >= self.MARK_L):
      self.L = 1
      MarkBF = MarkBF - self.MARK_L
    if (MarkBF >= self.MARK_M):
      self.M = 1
      MarkBF = MarkBF - self.MARK_M


#--------------------------------------------------------------------
# 
# Informationen über die Segmente eines Kurses
# Die Segmentinformation wird direkt aus den TrackTabellen
# ausgelesen und für die weitere Verarbeitung in dieser
# Klasse abgespeichert.
#
class track_segment_t:
  Mark : track_marker_t
  Geo: int
  n: int
  c0: float
  c1: float
  i_s: int
  i_e: int

  def __init__(self):
    self.Mark = track_marker_t()

  def clear(self):
    self.Mark.clear()


#--------------------------------------------------------------------
# 
# Klasse zum Laden der Kurstabelle und generieren der 
# Track-Informationen.
#
class sim_track_t:
  def __init__(self, TrackName, start_position=[0, 0, pi/2, 0]):
    # Tracktabelle laden. Diese muss in 'kurstabellen.py' als
    # numpy-Array hinterlegt sein.
    if (TrackName == "CaroloCup_Beispiel_6"):
      #  Kurs_CaroloCup_Beispiel_6     Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_CC_Beispiel_6_TrackTable
    elif (TrackName == "CaroloCup_Beispiel2_6"):
      #  Kurs_CaroloCup_Beispiel2_6     Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_CC_Beispiel2_6_TrackTable
    elif (TrackName == "CaroloCup_2015_Aula_6"):
      #  Kurs_CaroloCup_2015_6         Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_CC_2015_6_TrackTable
      #pass
    elif (TrackName == "CaroloCup_2015_Aula_6_M"):
      #  Kurs_CaroloCup_2015_6         Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_CC_2015_6_MIRROR_TrackTable
      #TrackTable = Kurs_CC_2015_6_MIRROR_TrackTable
      #pass
    elif (TrackName == "CaroloCup_2016_Stadthalle_6"):
      #  Kurs_CaroloCup_2016_6         Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_CC_2016_6_TrackTable
      #pass
    elif (TrackName == "CaroloCup_Gerade_6"):
      #  Kurs_Gerade                   Streckendefinitionstabellen laden
      pass
    elif (TrackName == "CaroloCup_Kreis_100_6"):
      #  Kurs_Kreis_100                Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_Kreis_100_TrackTable
    elif (TrackName == "CaroloCup_Kreis_250_6"):
      #  Kurs_Kreis_250                Streckendefinitionstabellen laden
      pass
    elif (TrackName == "CaroloCup_Kreis_25_6"):
      #  Kurs_Kreis_25                 Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_Kreis_25_TrackTable
    elif (TrackName == "CaroloCup_Kreis_50_6"):
      #  Kurs_Kreis_50                 Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_Kreis_50_TrackTable
    elif (TrackName == "EgoTrack_Testkurs_A_6"):
      #  Kurs_ET_A                     Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_ET_A_TrackTable
    elif (TrackName == "IPP_Testkurs_1"):
      #  Kurs_ET_A                     Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_IPP_1_TrackTable
    elif (TrackName == "IPP_Testkurs_2"):
      #  Kurs_ET_A                     Streckendefinitionstabellen laden
      TrackTable = kt.Kurs_IPP_2_TrackTable
    else:
      print('Kurs nicht vorhanden!\n')
      return

    # Stützpunkte des Kursverlaufs generieren
    # xh: Mittelstreifen = Definitionslinie auf die sich die Angaben in den
    #                      Streckendefinitionstabellen beziehen
    # xl: Linke Markierung
    # xm: Mittlere Markierung = entspricht im Wesentlichen xh aber für 
    #                           spätere Trennung separiert
    # xr: Rechte Markierung
    # xt: Mitte des rechten Fahrstreifens (=Solltrajektorie)

    # Überprüfen, ob das Format der Tracktabelle unterstützt wird
    if (TrackTable.shape[1] < 7):
      print('Tracktabellen < Version 5.0 werden nicht mehr unterstützt!\n')
      return

    n_seg = TrackTable.shape[0]

    # Indizes für die Spalten der TrackTable definieren
    IDX_ID  = 0  # ID
    IDX_G   = 1  # Gerade || Kurve
    IDX_M   = 2  # Markierung
    IDX_ET  = 3  #
    IDX_ER  = 4  #
    IDX_N   = 5  # Iterationen
    IDX_C   = 6  # Krümmung C0

    # Der Kurs wird erzeugt durch Abfahren mit einem einfachen Fahrzeugmodell
    # (nach Corke). Solange nur Geraden und Kreisbögen als
    # Konstruktionselemente dienen wäre dies auch anders realisierbar. Sobald
    # man auch Clothoiden erzeugen möchte, sollte dies hiermit relativ
    # problemlos machbar sein, indem man einfach eine konstante
    # Lenkwinkeländerung auf das Modell gibt.
    # Derzeit fährt das Fahrzeug mit v=10 m/s bei einer Abtastrate von
    # T=0.01s. Daraus folgt, dass pro Zeiteinheit ein Weg von 0.1m
    # zurückgelegt wird. Die daraus folgenden Positionen dienen in der
    # Simulation als Stützpunkte zur Erzeugung der Strecke und zur Bestimmung
    # der Relativlage des Ego-Fahrzeugs (und der Hindernisse) zum Kurs. Bei
    # Verkleinerung von v oder T (eigentlich ist nur das Produkt vT wichtig)
    # ergibt sich ein geringerer Abstand der Stützpunkte und damit eine
    # höhere Genauigkeit der Simulation. Dies geht natürlich auf Kosten des
    # notwendigen Speicherplatzes und vor allem auf Kosten der Rechenzeit,
    # die damit deutlich ansteigt.
    # Anmerkung: Eine Änderung von v oder T könnte derzeit zu Fehlern führen,
    # da ggf. noch an anderen Stellen Abhängigkeiten von den aktuellen Werten
    # durch Hard-Codierung bestehen!
    #-------------------------------------------------
    v   = 10.0    # Geschwindigkeit des Spurfahrzeugs
    AA  = 2.5     # Achsabstand des Spurfahrzeugs
    T   = 0.01    # Abtastintervall
    dL  = v*T     # Inkrement des Weges je Zeitschritt
    Lambda = 0.0  # Lenkwinkel
    BF = 3.5      # Breite eines Fahrstreifens
    BF2 = BF/2
    #-------------------------------------------------
    n_step = 1 # Anzahl der Stützpunkte der Fahrspur
    i_step = 0 # Laufvariable für die Stützpunkte der Fahrspur
    for i_Track in range(0, n_seg):
      n_step = n_step + int(T/0.01*TrackTable[i_Track, IDX_N])

    # Anlegen der Segment-Liste mit den Meta-Informationen über die Spur
    # (Markierungsart, Gerade/Kurve etc.)
    self.segment = [track_segment_t() for i_seg in range(n_seg)]

    # Anlegen der Matrix für die Stützstellen. Jede Zeile der Matrix enthält später
    # alle Informationen zu einem Stützpunkt.
    # [x-Position, y-Position, Kurswinkel psi, Krümmung c0, Segmentnummer, Reserve]
    self.xh = np.zeros((n_step, 6), dtype=np.float32)
    self.xnt = np.zeros((n_step,2), dtype=np.float32)
    #-------------------------------------------------
    x = self.xh[0, 0:7] # Referenz auf die 0. Zeile von xh
    # Momentan fest verdrahtete Startposition
    #x[0:4] = [0, 0, pi/2, 0]
    x[0:4] = start_position #[0, 0, pi/2, 0]
    # psi normieren / Zustand um c0 und n_s ergänzen
    x[[2,4,5]] = [x[2]%(2*pi), 0, 1]
    self.xnt[0,:] = [cos(x[2]),sin(x[2])]
    A = np.array([[1, 0, 0 ,0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 0]], dtype=np.float32)
    B = np.array([T*cos(x[2]), T*sin(x[2]), T*tan(Lambda)/AA, T])
    u = np.array([v])

    i_step = i_step + 1

    # In der folgenden Schleifen wird nun über alle Segmente des Tracks iteriert.
    # Entsprechend der Parameter, insbesondere c0 werden für jedes Segment die 
    # Stützpunkte auf der Skelettlinie xh berechnet.
    for i_seg in range(0, n_seg):
      # Anzahl der Stützpunkte des Segments
      n_seg_step = int(T/0.01*TrackTable[i_seg, IDX_N])
      self.segment[i_seg].n    = n_seg_step

      # Markierungsinformationen aus der Tracktabelle auslesen, decodieren und
      # im Segment explizit vermerken.
      MarkBF = int(TrackTable[i_seg, IDX_M])
      self.segment[i_seg].Mark.setMarkBF(MarkBF)

      # Geometrieinfo des Segments. Im Moment nur Gerade oder Kreisbogen
      self.segment[i_seg].Geo  = int(TrackTable[i_seg, IDX_G])

      # Lenkwinkel auslesen und daraus c0 bestimmen. Im Moment nur Kreisbögen mit c1 = 0 möglich.
      Lambda = TrackTable[i_seg, IDX_C]
      c0 = tan(Lambda)/AA
      self.segment[i_seg].c0   = c0
      # c1 momentan noch nicht berücksichtigt in den TrackTabellen
      self.segment[i_seg].c1   = 0.0
      # Start-Stützpunkt des Segments
      self.segment[i_seg].i_s  = i_step
      # End-Stützpunkt des Segments
      self.segment[i_seg].i_e  = i_step + n_seg_step

      # Hier die Iteration über alle Stützpunkte des Segments
      for i_seg_step in range(0, n_seg_step):
        xo = self.xh[i_step-1, 0:7] # Referenz auf x[k]
        xn = self.xh[i_step  , 0:7] # Referenz auf x[k+1]
        B = np.array([T*cos(xo[2]), T*sin(xo[2]), T*tan(Lambda)/AA, T])

        xn[0:4] = np.matmul(A, xo[0:4].transpose()) + B * u
        # psi normieren / Zustand um c0 und n_s ergänzen
        xn[[2,4,5]] = [xn[2]%(2*pi), c0, i_seg]
        self.xnt[i_step,:] = [cos(xn[2]),sin(xn[2])]
      
        i_step = i_step + 1

    self.TrackLen = (self.xh.shape[0]-1)*dL
    #print("Streckenlänge= %6.2f\n" %((self.xh.shape[0]-1)*0.1))
    print("Streckenlänge= %6.2f\n" %(self.TrackLen))

    #-----------------------------------------------------------------------------
    # Hier werden aus der Skelettlinie (xh) die restlichen Markierungen erzeugt.
    # Linke Markierung
    self.xl = np.zeros_like(self.xh)
    # Mittlere Markierung (gestrichelt!)
    self.xm = np.zeros_like(self.xh)
    # Rechte Markierung
    self.xr = np.zeros_like(self.xh)
    # Solltrajektorie in rechter Spur
    self.xtr = np.zeros_like(self.xh)
    # Solltrajektorie in linker Spur
    self.xtl = np.zeros_like(self.xh)

    for i_step in range(0, n_step):
      sa = sin(self.xh[i_step,2])
      ca = cos(self.xh[i_step,2])

      if (abs(self.xh[i_step,4]) < 0.00001): # bei sehr kleinem c0 wird eine Gerade angenommen
        self.xr[i_step,:]  = [self.xh[i_step, 0]+BF*sa,  self.xh[i_step, 1]-BF*ca,  self.xh[i_step, 2], self.xh[i_step, 3],            0,              self.xh[i_step, 5]]
        self.xl[i_step,:]  = [self.xh[i_step, 0]-BF*sa,  self.xh[i_step, 1]+BF*ca,  self.xh[i_step, 2], self.xh[i_step, 3],            0,              self.xh[i_step, 5]]
        self.xm[i_step,:]  = [self.xh[i_step, 0],        self.xh[i_step, 1],        self.xh[i_step, 2], self.xh[i_step, 3],            0,              self.xh[i_step, 5]]
        self.xtr[i_step,:] = [self.xh[i_step, 0]+BF2*sa, self.xh[i_step, 1]-BF2*ca, self.xh[i_step, 2], self.xh[i_step, 3],            0,              self.xh[i_step, 5]]
        self.xtl[i_step,:] = [self.xh[i_step, 0]-BF2*sa, self.xh[i_step, 1]+BF2*ca, self.xh[i_step, 2], self.xh[i_step, 3],            0,              self.xh[i_step, 5]]
      else:
        rh = 1/self.xh[i_step, 4]
        
        self.xr[i_step,:]  = [self.xh[i_step, 0]+BF*sa,  self.xh[i_step, 1]-BF*ca,  self.xh[i_step, 2], self.xh[i_step, 3]*(rh+BF)/rh,  1/(rh+BF),     self.xh[i_step, 5]]
        self.xl[i_step,:]  = [self.xh[i_step, 0]-BF*sa,  self.xh[i_step, 1]+BF*ca,  self.xh[i_step, 2], self.xh[i_step, 3]*(rh-BF)/rh,  1/(rh-BF),     self.xh[i_step, 5]]
        self.xm[i_step,:]  = [self.xh[i_step, 0],        self.xh[i_step, 1],        self.xh[i_step, 2], self.xh[i_step, 3],             self.xh[i_step, 4], self.xh[i_step, 5]]
        self.xtr[i_step,:] = [self.xh[i_step, 0]+BF2*sa, self.xh[i_step, 1]-BF2*ca, self.xh[i_step, 2], self.xh[i_step, 3]*(rh+BF2)/rh, 1/(rh+BF2),    self.xh[i_step, 5]]
        self.xtl[i_step,:] = [self.xh[i_step, 0]-BF2*sa, self.xh[i_step, 1]+BF2*ca, self.xh[i_step, 2], self.xh[i_step, 3]*(rh-BF2)/rh, 1/(rh-BF2),    self.xh[i_step, 5]]
  
#--------------------------------------------------------------------
  def getTrack(self):
    return self.xh, self.xr, self.xl, self.xm, self.xtr, self.xtl, self.xnt, self.segment
#--------------------------------------------------------------------

