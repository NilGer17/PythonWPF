import numpy as np
import matplotlib.pyplot as plt
#öffnet das main skript, falls müll in der datei steht
exec(open("main.py").read())

def plot(Numbers, Color, sub):
    Stützstellen = np.linspace(0,2*np.pi, 101)
    sub.plot(Stützstellen,Numbers, Color)
    sub.grid()
    sub.set_xlabel("x")
    sub.set_ylabel("y")

datei = open("sinoutData", "r")
#Zeilen einlesen
lines = datei.readlines()
#print(lines)
Stützstellen = np.linspace(0,2*np.pi, 101)
Output = ["r-", "b--", "k+", "r"]
megaListofNumbers = []
for line in lines:
    listOfNumbers = []
    numbers = line.split()
    
    for numb in numbers:
        listOfNumbers.append(float(numb))   
    #print(listOfNumbers)
    megaListofNumbers.append(listOfNumbers)
    #ar = np.array(listOfNumbers,np.float64)
    #print((ar))
    #plt.plot(Stützstellen, ar, Output[])
    #plt.plot(Stützstellen, float(line))
#plt.show()
print(megaListofNumbers)
i = 0
fig, axs = plt.subplots(4)
for Numbers in megaListofNumbers:
    plot(Numbers, Output[i], axs[i])
    i+= 1

axs[3].plot(Stützstellen, np.exp(Stützstellen*-0.5), "r--")
axs[3].plot(Stützstellen, -np.exp(Stützstellen*-0.5), "r--")

fig.legend(["sin(x)","sin(3x)","sin^2(x)"])
plt.show()
datei.close()