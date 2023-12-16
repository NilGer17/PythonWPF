
import numpy as np
from math import atan

AA  = 2.5   # Achsabstand des "Spur-Fahrzeugs"

LF_13_5   = atan(AA/(10.0+3.5))  # Lenkwinkel für Radius 13.5m
LF_13_0   = atan(AA/(10.0+3.0))  # Lenkwinkel für Radius 13.0m
LF_18_0   = atan(AA/(10.0+8.0))  # Lenkwinkel für Radius 18.0m
LF_25_0   = atan(AA/(25.0))      # Lenkwinkel für Radius 25.0m
LF_50_0   = atan(AA/(50.0))      # Lenkwinkel für Radius 50.0m
LF_100_0  = atan(AA/(100.0))     # Lenkwinkel für Radius 100.0m
LF_250_0  = atan(AA/(250.0))     # Lenkwinkel für Radius 250.0m

# Markierung:
#   0 - keine Markierung
#   1 - Seitenmarkierung R  MR
#   2 - Mittelmarkierung    MM
#   4 - Seitenmarkierung L  ML
#   8 - SM + SLR-E          SLRE
#  16 - SM + SLL-A          SLLA
#  32 -                     SLLA
#  64 -                     SLLE
# 128 -                     P   
#
# Die Markierungen für die gesamte Fahrspur ergeben sich durch Addition
# der einzelnen Tags, also z.B. 1 (MR) + 2 (MM) + 4 (ML) = 7.

#--------------------------------------------------------------------
# Kreis-Kurse mit unterschiedlichen Radien
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_Kreis_25_TrackTable = np.array([[  1, 0,  7,  0, 0,  1570, +LF_25_0]])
Kurs_Kreis_50_TrackTable = np.array([[  1, 0,  7,  0, 0,   3140, +LF_50_0]])
Kurs_Kreis_100_TrackTable = np.array([[  1, 0,  7,  0, 0,  6280, +LF_100_0]])


#--------------------------------------------------------------------
# CC-Beispiel-Kurs (Regelwerk)
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_CC_Beispiel_6_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   20+1,      0.0,         10],
                  # Parkstreifen
                  [2,   0,   7+128, 0,   0,   547+1,     0.0,         10],
                  [3,   0,   7,     0,   0,   20+1,      0.0,         10],
                  [4,   1,   7,     0,   0,   318+1,     +LF_13_5,    8],
                  [5,   0,   7,     0,   0,   262+1,     0.0,         12],
                  # 1. Kreuzung
                  [6,   0,   0,     1,   16,  69+1,      0.0,         12],
                  [7,   0,   7,     0,   0,   198+1,     0.0,         11],
                  # 2. Kreuzung
                  [8,   0,   0,     1,   12,  69+1,      0.0,         11],
                  [9,   0,   7,     0,   0,   98+1,      0.0,         10],
                  [10,  1,   7,     0,   0,   636+1,     +LF_13_5,    8],
                  # Stoplinie rechts
                  [11,  0,   7+16,  0,   0,   99+1,      0.0,         10], #SLR-E
                  # 2. Kreuzung
                  [12,  0,   0,     2,   8,   68+1,      0.0,         12],
                  # Stoplinie links
                  [13,  0,   7+32,  0,   0,   81+1,      0.0,         11], # SLL-A
                  [14,  1,   7,     0,   0,   424+1,     -LF_13_5,    8],
                  # Stoplinie rechts
                  [15,  0,   7+16,  0,   0,   82+1,      0.0,         10], # SLR-E
                  # 1. Kreuzung
                  [16,  0,   0,     2,   6,   68+1,      0.0,         10], 
                  # Stoplinie links
                  [17,  0,   7+32,  0,   0,   257+1,     0.0,         12], # SLL-A
                  [18,  1,   7,     0,   0,   212+1,     -LF_13_5,    8],
                  [19,  1,   7,     0,   0,   318+1,     +LF_13_5,    8], 
                  [20,  0,   7,     0,   0,   5+1,       0.0,         8],
                  [21,  1,   7,     0,   0,   199+2+2,     +LF_13_0,    8], # 199+1
                  [22,  0,   7,     0,   0,   11+1,      0.0,         8],
                  [23,  0,   7,     0,   0,   20+1-9,      0.0,         8]])


#--------------------------------------------------------------------
# CC-Beispiel-Kurs (Regelwerk)
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
m = 2.0
Kurs_CC_Beispiel2_6_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   m*(20+1),      0.0,         10],
                  # Parkstreifen
                  [2,   0,   7+128, 0,   0,   m*(547+1),     0.0,         10],
                  [3,   0,   7,     0,   0,   m*(20+1),      0.0,         10],
                  [4,   1,   7,     0,   0,   m*(318+1),     (+LF_13_5)/m,    8],
                  [5,   0,   7,     0,   0,   m*(262+1),     0.0,         12],
                  # 1. Kreuzung
                  [6,   0,   0,     1,   16,  (69+1+4),      0.0,         12],
                  [7,   0,   7,     0,   0,   m*(198+1)+69+1-4+7,     0.0,         11],
                  # 2. Kreuzung
                  [8,   0,   0,     1,   12,  (69+1+4+1),      0.0,         11],
                  [9,   0,   7,     0,   0,   m*(98+1)+60-4-6-2,      0.0,         10],
                  [10,  1,   7,     0,   0,   m*(636+1),     (+LF_13_5)/m,    8],
                  # Stoplinie rechts
                  [11,  0,   7+16,  0,   0,   m*(99+1)+47,      0.0,         10], #SLR-E
                  # 2. Kreuzung
                  [12,  0,   0,     2,   8,   (68+1)+1,      0.0,         12],
                  # Stoplinie links
                  [13,  0,   7+32,  0,   0,   m*(81+1),      0.0,         11], # SLL-A
                  [14,  1,   7,     0,   0,   m*(424+1),     (-LF_13_5)/m,    8],
                  # Stoplinie rechts
                  [15,  0,   7+16,  0,   0,   m*(82+1)-15,      0.0,         10], # SLR-E
                  # 1. Kreuzung
                  [16,  0,   0,     2,   6,   (68+1)+2,      0.0,         10], 
                  # Stoplinie links
                  [17,  0,   7+32,  0,   0,   m*(257+1)+45,     0.0,         12], # SLL-A
                  [18,  1,   7,     0,   0,   m*(212+1+10),     (-LF_13_5)/m,    8],
                  [19,  1,   7,     0,   0,   m*(318+1+10),     (+LF_13_5)/m,    8], 
                  [20,  0,   7,     0,   0,   m*(5+1+16),       0.0,         8],
                  [21,  1,   7,     0,   0,   m*(199+2+12),     (+LF_13_0)/m,    8], # 199+1
                  [22,  0,   7,     0,   0,   m*(11+1),      0.0,         8],
                  [23,  0,   7,     0,   0,   m*(20+1+1),      0.0,         8]])


#--------------------------------------------------------------------
# Einfacher Rundkurs ohne Kreuzungen
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_ET_A_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   500+1,     0.0,         10],
                  [2,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [3,   0,   7,     0,   0,   500+1,     0.0,         10],
                  [4,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [5,   0,   7,     0,   0,   500+1,     0.0,         10],
                  [6,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [7,   0,   7,     0,   0,   500+1,     0.0,         10],
                  [8,   1,   7,     0,   0,   392+1,     +LF_25_0,     8]])


#--------------------------------------------------------------------
# Einfacher Rundkurs ohne Kreuzungen
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_IPP_1_TrackTable = np.array([
                  [1,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [2,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [3,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [4,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [5,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [6,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [7,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [8,   1,   7,     0,   0,   392+1,     +LF_25_0,     8]])


#--------------------------------------------------------------------
# Einfacher Rundkurs ohne Kreuzungen
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_IPP_2_TrackTable = np.array([
                  [1,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [2,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  #[3,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [3,   0,   7,     0,   0,   300+1,     0.0,         10],
                  [4,   1,   7,     0,   0,   80,        +LF_13_5,    10],     
                  [5,   1,   7,     0,   0,   80,        -LF_13_5,    10],
                  [6,   1,   7,     0,   0,   80,        -LF_13_5,    10],
                  [7,   1,   7,     0,   0,   80,        +LF_13_5,    10],
                  [8,   0,   7,     0,   0,   400+1,     0.0,         10],
                  [10,   0,   7,     0,   0,   300+1,     0.0,         10],
                  [11,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [12,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [13,   1,   7,     0,   0,   392+1,     +LF_25_0,     8],
                  [14,   0,   7,     0,   0,  1300+1,     0.0,         10],
                  [15,   1,   7,     0,   0,   392+1,     +LF_25_0,     8]])


#--------------------------------------------------------------------
# CC-2016-Kurs (Stadthalle BS)
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_CC_2016_6_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   20,      0.0],
                  # Parkstreifen
                  [2,   0,   7+128, 0,   0,   338,     0.0],
                  [3,   0,   7,     0,   0,   20,      0.0],
                  [4,   1,   7,     0,   0,   212,     +LF_13_5],  #211
                  [5,   0,   7,     0,   0,   734,     0.0],
                  [6,   1,   7,     0,   0,   80,      +LF_13_5],
                  [7,   1,   7,     0,   0,   80,      -LF_13_5],
                  [8,   1,   7,     0,   0,   80,      -LF_13_5],
                  [9,   1,   7,     0,   0,   80,      +LF_13_5],
                  [10,  0,   7,     0,   0,   200,     0.0],
                  [11,  1,   7,     0,   0,   212,     +LF_13_5],
                  [12,  0,   7,     0,   0,   30,      0.0],
                  [13,  1,   7,     0,   0,   106,     +LF_13_5],
                  [14,  0,   7,     0,   0,   76,      0.0],
                  # 1.Kreuzung
                  [15,  0,   0,     1,   21,  68,      0.0],
                  [16,  0,   7,     0,   0,   154,     0.0],
                  [17,  1,   7,     0,   0,   318,     -LF_13_5],
                  [18,  0,   7,     0,   0,   80,      0.0],
                  [19,  1,   7,     0,   0,   318,     -LF_13_5],
                  # Stoplinie rechts
                  [20,  0,   7+16,  0,   0,   155,     0.0],
                  # 1.Kreuzung
                  [21,  0,   0,     2,   15,  68,      0.0],
                  # Stoplinie links
                  [22,  0,   7+32,  0,   0,   75,      0.0],
                  [23,  1,   7,     0,   0,   380,     -LF_13_5],
                  [24,  1,   7,     0,   0,   126,     +LF_13_5],
                  [25,  0,   7,     0,   0,   105,     0.0],
                  [26,  1,   7,     0,   0,   146,     +LF_13_5],
                  [27,  0,   7,     0,   0,   80,      0.0],
                  [28,  1,   7,     0,   0,   340,     +LF_13_5],
                  [29,  1,   7,     0,   0,   444,     -LF_13_5],
                  # Stoplinie rechts
                  [30,  0,   7+16,  0,   0,   117,     0.0],
                  # 2.Kreuzung
                  [31,  0,   0,     2,   37,  68,      0.0],
                  # Stoplinie links
                  [32,  0,   7+32,  0,   0,   133,     0.0],
                  [33,  1,   7,     0,   0,   318,     +LF_13_5],
                  [34,  0,   7,     0,   0,   50,      0.0],
                  [35,  1,   7,     0,   0,   318,     +LF_13_5],
                  [36,  0,   7,     0,   0,   134,     0.0],   
                  # 2.Kreuzung
                  [37,  0,   0,     1,   31,  68,      0.0],
                  [38,  0,   7,     0,   0,   96,      0.0],
                  [39,  1,   7,     0,   0,   317,     +LF_13_5],   # 314
                  [40,  0,   7,     0,   0,   350,     0.0],        # 343
                  [41,  1,   7,     0,   0,   210,     +LF_13_5],
                  [42,  0,   7,     0,   0,   37,      0.0]])


#--------------------------------------------------------------------
# CC-2015-Kurs (Aula TU BS)
# Aufbau der Tabellen: [ID  Gerade/Kurve  Markierung  ...  ...  Iterationen  Lenkwinkel]
Kurs_CC_2015_6_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   20,     0.0],
                  # Parkstreifen
                  [2,   0,   7+128, 0,   0,   556,    0.0],
                  [3,   0,   7,     0,   0,   20,     0.0],
                  [4,   1,   7,     0,   0,   212,    +LF_13_5],
                  [5,   0,   7,     0,   0,   500,    0.0],
                  [6,   1,   7,     0,   0,   318,    +LF_13_5],
                  [7,   0,   7,     0,   0,   136,    0.0],
                  # 1.Kreuzung
                  [8,   0,   0,     1,   17,  69+1,     0.0],
                  [9,   0,   7,     0,   0,   93+4,     0.0],
                  [10,  1,   7,     0,   0,   102,    +LF_13_5],
                  [11,  0,   7,     0,   0,   150,    0.0],
                  [12,  1,   7,     0,   0,   212,    +LF_13_5],
                  [13,  0,   7,     0,   0,   80,     0.0],
                  [14,  1,   7,     0,   0,   504,    +LF_18_0],
                  [15,  1,   7,     0,   0,   56,     -LF_13_5],
                  # Stoplinie rechts
                  [16,  0,   7+16,  0,   0,   100+2,    0.0],
                  # 1.Kreuzung
                  [17,  0,   0,     2,   8,   69+3,     0.0],
                  # Stoplinie links
                  [18,  0,   7+32,  0,   0,   159,    0.0],
                  [19,  1,   7,     0,   0,   424,    +LF_13_5],
                  [20,  0,   7,     0,   0,   40,     0.0],
#                  [21,  1,   7,     0,   0,   318,    -LF_13_5],
                  [21,  1,   7,     0,   0,   109,    -LF_13_5],
                  [22,  1,   3,     0,   0,   100,    -LF_13_5],
                  [23,  1,   7,     0,   0,   109,    -LF_13_5],
                  [24,  0,   7,     0,   0,   20,     0.0],
                  [25,  1,   7,     0,   0,   208,    +LF_13_5],
                  [26,  0,   7,     0,   0,   29,     0.0], # 12
                  [27,  1,   7,     0,   0,   215,    +LF_13_5], # 208
                  [28,  0,   7,     0,   0,   30+7,     0.0]]) # 25

Kurs_CC_2015_6_MIRROR_TrackTable = np.array([
                  [1,   0,   7,     0,   0,   20,     0.0],
                  # Parkstreifen
                  [2,   0,   7+128, 0,   0,   556,    0.0],
                  [3,   0,   7,     0,   0,   20,     0.0],
                  [4,   1,   7,     0,   0,   212,    -LF_13_5],
                  [5,   0,   7,     0,   0,   500,    0.0],
                  [6,   1,   7,     0,   0,   318,    -LF_13_5],
                  [7,   0,   7,     0,   0,   136,    0.0],
                  # 1.Kreuzung
                  [8,   0,   0,     1,   17,  69+1,     0.0],
                  [9,   0,   7,     0,   0,   93+4,     0.0],
                  [10,  1,   7,     0,   0,   102,    -LF_13_5],
                  [11,  0,   7,     0,   0,   150,    0.0],
                  [12,  1,   7,     0,   0,   212,    -LF_13_5],
                  [13,  0,   7,     0,   0,   80,     0.0],
                  [14,  1,   7,     0,   0,   504,    -LF_18_0],
                  [15,  1,   7,     0,   0,   56,     +LF_13_5],
                  # Stoplinie rechts
                  [16,  0,   7+16,  0,   0,   100+2,    0.0],
                  # 1.Kreuzung
                  [17,  0,   0,     2,   8,   69+3,     0.0],
                  # Stoplinie links
                  [18,  0,   7+32,  0,   0,   159,    0.0],
                  [19,  1,   7,     0,   0,   424,    -LF_13_5],
                  [20,  0,   7,     0,   0,   40,     0.0],
#                  [21,  1,   7,     0,   0,   318,    -LF_13_5],
                  [21,  1,   7,     0,   0,   109,    +LF_13_5],
                  [22,  1,   3,     0,   0,   100,    +LF_13_5],
                  [23,  1,   7,     0,   0,   109,    +LF_13_5],
                  [24,  0,   7,     0,   0,   20,     0.0],
                  [25,  1,   7,     0,   0,   208,    -LF_13_5],
                  [26,  0,   7,     0,   0,   29,     0.0], # 12
                  [27,  1,   7,     0,   0,   215,    -LF_13_5], # 208
                  [28,  0,   7,     0,   0,   30+7,     0.0]]) # 25