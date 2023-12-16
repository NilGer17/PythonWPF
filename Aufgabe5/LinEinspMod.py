#!/usr/bin/python3
"""
IPP - Ingenieurwissenschaftliches Programmieren mit Python
Aufgabe A-5.2

Beispiellösung mit der Ergänzung um animierte Plots

(c) Prof. Dr.-Ing. Volker von Holt / Fahrzeuginformatik
"""
# Importieren der notwendigen Module
import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------
# Initialisierungen
#---------------------------------------
# Abtastzeit
T = 0.1
L = 2.5   # Radstand in [m]

#---------------------------------------
# Anlegen der Datenstrukturen
#---------------------------------------
# Berechnung der Gesamtdauer des "Versuchs"
t_gesamt = 60.0   # Zum Testen ausnahmsweise fest vorgegeben
print('Gesamtzeit= ', t_gesamt)

# Berechnung der Anzahl Samples => Allokierung der Datenfelder
n_gesamt = int(t_gesamt/T)+1        # +1 damit Anfangs- und Endwert dabei sind
print('Samples= ', n_gesamt)

# Für einen Test des Querdynamikmodells ist es sinnvoll, zunächst v=const. anzusetzen,
# da sich dann bei Lambda=const. auch konstante Krümmungsradien ergeben, die gut zu 
# kontrollieren sind.
v_test = 10.0    # v=const. in [m/s]
# v als NumPy-Array über alle Samples
v = v_test*np.ones(n_gesamt, dtype=np.float32)  # v = const. [m/s]


# Lenkwinkel für gerade Abschnitte (c0) und für Kurvenabschnitte (c1)
Lambda_c0 = 0.0/180.0*np.pi      # Lenkwinkel Geradeausfahrt in [rad]
Lambda_c1 = 2.5/180.0*np.pi      # Lenkwinkel Kurvenfahrt links in [rad]

#Zum Test
Lambda_c2 = -2/180.0*np.pi

# Lambda als NumPy-Array über alle Samples
# Die Initialisierung erfolgt dieses Mal nicht anhand einer Datei, sondern 
# durch direkte Vorgabe. Die Werte für Lambda sowie die Intervallgrößen sind 
# natürlich nur Beispiele. 
Lambda = np.ones_like(v)
Lambda[:90]     = Lambda_c1
Lambda[90:120]  = Lambda_c0
Lambda[120:210] = Lambda_c1
Lambda[210:300] = Lambda_c0
Lambda[300:390] = Lambda_c1
Lambda[390:420] = Lambda_c0
Lambda[420:510] = Lambda_c1
Lambda[510:]    = Lambda_c0
#print(Lambda)

"""
Hier muss nun die Berechnung der Positionsdaten (x,y,psi) entsprechend der v- und Lambda-Werte erfolgen.
...
...
...
"""
#p stellt Vektor aus (x,y,psi) dar, gleiche größe wie die Geschwindigkeitsvektor
p = np.zeros((n_gesamt,3),dtype=np.float32)
# Startzustand ist alles auf Null
#p(x,y,psi) ?? p[:,0] = x | p[:,1] = y | p[:,2] = psi
p[0,:] = [0,0,0]
#für jedes k aus dem Lambdas/Geschwindigkeiten
#x[k+1] = x[k] + T*v[k]*cos(psi[k])
#y[k+1] = y[k] + T*v[k]*sin(psi[k])
#psi[k+1] = psi[k] + T*v[k]*tan(Lambda[k]/L)
for k in range(0,Lambda.shape[0]-1):
    p[k+1,0] = p[k,0] + T * v[k]*np.cos(p[k,2]) #x
    p[k+1,1] = p[k,1] + T * v[k]*np.sin(p[k,2]) #y
    p[k+1,2] = p[k,2] + T * v[k]*np.tan(Lambda[k]/L) #psi
    #print("Lambda[k]= ", Lambda[k]) 
#p Vektor gefüllt!
"""
Hier folgt dann noch die grafische Ausgabe - sinnvollerweise als x/y-Plot, damit die Bahn gut zu erkennen ist.
...
...
...
"""
# Wir geben 1 Subplot
fig, ax = plt.subplots()
#---------------------------------------
# Plot-Variante 2: Plot animieren über der Zeit - später wichtig für Live-Plots
#---------------------------------------
dT = 0.5        # Zeit-Delta zwischen Animationsschritten
t  = 0.0        # Laufende Zeit
dn = 5          # Sample-Delta zwischen Animationsschritten
n  = dn         # Laufender Sample-Index
dt_pause = 0.05   # für dT läuft die Animation in "Echtzeit", für < dT schneller, für > dT langsamer
#
Fzg, = ax.plot(p[:,0], p[:,1])
ax.grid()
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.legend(['Fahrzeug'])
plt.pause(dt_pause)
while t < t_gesamt:
    Fzg.set_data(p[:n,0], p[:n,1])  # update the data
    #Pfeil in aktuelle Lenkrichtung -> arrow(x,y,dx,dy,properties)
    arw = ax.arrow(p[n,0], p[n,1],30*np.cos(p[n,2]), 30*np.sin(p[n,2]), figure=fig, color='red', linewidth=2,head_width = 3)
    n += dn
    t += dT
    plt.pause(dt_pause)
    #print("Vorher:",id(arw))
    arw.remove()
    #print("Nachher:" ,id(arw))
plt.show()
