import numpy as np
import matplotlib.pyplot as plt

#-------
#Einlesen der Bewegungsdatei
V_Dat = np.transpose(np.loadtxt("GeschDaten.txt"))
dT = V_Dat[0]
v_Soll = V_Dat[1]
T = 0.1
step = 0
dTreal = dT[0]
aReal =[]
v = []
v.append(1)
s = []
s.append(0)
#x = []
#x.append(0)
x = np.array()
#print(v)
A = np.matrix([[1, T, T**2/2],[0, 1, T],[0, 0, 1]])
for t in np.arange(0,60,T):
    if t>dTreal and step < len(dT)-1:
        step+=1
        dTreal = dTreal + dT[step]
    #print(a[step])
    aReal.append(a[step])
    v.append((a[step] *T)+v[-1])
    s.append((a[step]*T**2/2)+(v[-1]*T)+s[-1])
   # x.append(A+x[-1])
    pass

v.pop(0)
s.pop(0)
x.pop(0)
#print(dT, a)
#print(v)
q = np.arange(0,60,T)
fig, ax = plt.subplots(3)
ax[0].plot(q, aReal)
ax[0].set_xlabel("t in s")
ax[0].set_ylabel("a in m/s^2")
ax[0].set_title("Beschleunigung")
ax[1].plot(q, v)
ax[1].set_xlabel("t in s")
ax[1].set_ylabel("v in m/s")
ax[1].set_title("Geschwindigkeit")
ax[2].plot(q, s)
ax[2].set_xlabel("t in s")
ax[2].set_ylabel("s in m")
ax[2].set_title("Strecke")
#ax[3].plot(q, x)
print(x)
plt.show()