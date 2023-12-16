import numpy as np
from matplotlib import pyplot as plt

import Classes as CL

#s1, i1, i2, i3 = np.loadtxt("Klausurvorbereitung/Output1.txt", skiprows=1, unpack=1) #skipRow überspringt die 1, unpack notwendig zum transponieren
input = np.loadtxt("Klausurvorbereitung/Output1.txt", skiprows=1) #skipRow überspringt die 1, unpack notwendig zum transponieren
fig, ax = plt.subplots(2)
# ax[0].plot(s1, i1)
# ax[0].plot(s1, i2)
# ax[0].plot(s1, i3)
#plt.show()


Verarbeitung = CL.Verarbeiten(input)
#Verarbeitung.print_stuetzstellen()
#Verarbeitung.print_function_values()
all_crossings = (Verarbeitung.find_all_crossings()) 
print("Crossings")
Stuezstellen = Verarbeitung.get_stuetzstellen()
alleFunktionswerte = Verarbeitung.get_function_values()
print("Vals")
for Funktionswetrte in alleFunktionswerte:
    ax[0].plot(Stuezstellen, Funktionswetrte)
print("Plot")

for crossings_in_func in all_crossings:
    for crossing in crossings_in_func:
        ax[0].scatter(crossing[0], crossing[1] , color='black')
print("Scatter")

all_maximas = Verarbeitung.find_all_maxima()

for maximas in all_maximas:
    for singlemax in maximas:
        ax[0].scatter(singlemax[0], singlemax[1], color="red")


plt.show()
# def find_Schnittpunkt(fx1, fx2, s):
#     '''
#     Findet Schnittpunkte zweier Funktionen an den Stützstellen.

#     Args:
#     fx1 : Funktionswerte der ersten Funktion.
#     fx2 : Funktionswerte der zweiten Funktion.
#     s : Stützstellen.

#     Returns:
#     tuple: Ein Tupel mit zwei Listen:
#            1. Liste der Funktionswerte an den Schnittpunkten.
#            2. Liste der Stützstellen, an denen die Schnittpunkte liegen.

#     Details:
#     Die Funktion prüft, ob die Funktionswerte der Funktionen fx1 und fx2 sich an den Stützstellen s kreuzen.
#     Es werden alle Schnittpunkte ermittelt, indem zunächst fx1 als obere Funktion und dann fx2 als obere Funktion betrachtet wird.
#     '''
#     SchnittList = []
#     StList = []
#     for i in range(0, len(fx1), 1):
#         if( fx1[i-1] > fx2[i-1] and fx1[i] <= fx2[i]):
#             SchnittList.append(fx1[i])
#             StList.append(s[i])
#         if( fx1[i-1] < fx2[i-1] and fx1[i] >= fx2[i]):
#             SchnittList.append(fx1[i])
#             StList.append(s[i])
#     return list(zip(StList, SchnittList)) #macht aus beiden Listen jeweile ein Tupel, alle Tupekl werden zu einer neuen Liste gemacht


# #Schn, Stue = find_Schnittpunkt(i1,i2, s1)
# print(find_Schnittpunkt(i1, i3, s1))
# for xy in find_Schnittpunkt(i1, i3, s1):
#     ax[0].scatter(xy[0], xy[1] , color='black')
# for xy in find_Schnittpunkt(i1, i2, s1):
#     ax[0].scatter(xy[0], xy[1] , color='red')
# for xy in find_Schnittpunkt(i2, i3, s1):
#     ax[0].scatter(xy[0], xy[1], color='green' )
# #plt.show()

