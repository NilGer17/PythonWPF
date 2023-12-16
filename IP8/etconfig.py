## @package EgoTrack
"""
Konfigurationsgrößen in Form von Dictonaries für einzelne
Programmstrukturen. 
"""

# Konfiguration der Umgebung
env = {
  "ros"  : True,
  "rviz" : True,
  "mpl"  : False
}


# Konfiguration der Kursanzeige
figTrack = {
  # Festlegung der Höhe und Breite des Fensters zur Kursanzeige
  # Empfehlung: Bei den meisten Kursen ist ein quadratisches 
  # Fenster vorteilhaft. Ausnahme: Carolo-Cup 2016 (Stadthalle)
  # 10x10: Display > 2560x1440
  # 8x8:   Display > 1920x1080
  # 16x8 bzw. 12x6 für "Stadthallenkurs"
  "width"  : 10, # 8 | 16,
  "height" : 10, # 8 |  8,

  # Festlegung ob immer der ganze Kurs und nur ein Ausschnitt zentriert
  # um die momentane Position des EGO angezeigt werden soll.
  "viewport_focus" : False,   # True: Ausschnitt | False: ganzer Kurs
  "viewport_dim"   : 25,     # 1/2 Abmessung des Kursausschnitts

  # Festlegung, ob zur Beschleunigung Blitting genutzt werden soll.
  # Nur sinnvoll, bei konstanter Anzeige des ganzen Kurses, wird daher
  # im Viewport-Modus automatisch deaktiviert.
  "use_blitting" : True
}

# Allgemeine Parameter der Simulation
sim = {
  # Pause nach jeder Iteration
  "sim_pause"  : 0.0, #0.01, # (0.1) # (1.0)
  # Anzahl der zu fahrenden Kursrunden (bei "CaroloCup_Beispiel_6" >= 2)
  "sim_loops"  : 1,
  # Einzelschrittsteuerung der Simulation aktivieren
  # Steppen = Mouseclick in das Track-Window
  "singlestep" : False,
  # Simulationsschritte je Einzelschritt
  "n_singlestep" : 5,
  # Abtastzeit
  "dT" : 0.08
}

# Einige Angaben zum Eigenfahrzeug
ego = {
  # Achsabstand des EGO
  # Formparameter/Abmessungen des Fahrzeugs
  "AA" : 2.5,  # Achsabstand [m]
  "L"  : 4.0,  # Länge [m]
  "B"  : 2.0,  # Breite [m]

  #"ini_offset": [0.5, 0.5, -0.2],  # Initialer Lage-Offset zur Startposition der Ideal-Trajektorie
  "ini_offset": [0.5, +0.5, -0.2],  # Initialer Lage-Offset zur Startposition der Ideal-Trajektorie
  #"ini_offset": [0.0, 0.0, 0.0],  # Initialer Lage-Offset zur Startposition der Ideal-Trajektorie

  #"v_soll_max" : 16.0, # max. v-soll
  "v_soll_max" : 14.0, # max. v-soll
  "ay_max"     : 10.0, # max. a in Querrichtung

  "a_Tp" : 3.0, # Zeitkonstante für pos. ax
  "a_Tn" : 3.0, # Zeitkonstante für neg. ax

  "TLambda"     : 2.0,  # Zeitkonstante für den Lenkaktor
  "Lambda_max"  : 0.5   # max. Lenkwinkel +/- [rad]
}


# Auswahl des simulierten Kurses 
simTrack = {
  # Hier erfolgt die Definition und Auswahl des Kurses. Für die möglichen 
  # Kurse bitte in #kurstabellen.py' nachschauen.
  #"Kursname" : "CaroloCup_Beispiel_6"
  #"Kursname" : "CaroloCup_Beispiel2_6"
  #"Kursname" : "CaroloCup_2015_Aula_6"
  #"Kursname" : "CaroloCup_2015_Aula_6_M"
  #"Kursname" : "CaroloCup_2016_Stadthalle_6"
  #"Kursname" : "CaroloCup_Gerade_6"      # noch nicht implementiert
  #"Kursname" : "CaroloCup_Kreis_100_6" 
  #"Kursname" : "CaroloCup_Kreis_250_6"   # noch nicht implementiert
  #"Kursname" : "CaroloCup_Kreis_25_6"
  #"Kursname" : "CaroloCup_Kreis_50_6"
  #"Kursname" : "EgoTrack_Testkurs_A_6"
  #"Kursname" : "IPP_Testkurs_1"
  "Kursname" : "IPP_Testkurs_2"
}

   

