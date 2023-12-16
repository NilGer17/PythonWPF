#! usr/bin/python3

'''
Datei einlesen berechnen, anzeigen, ausgeben

'''

from matplotlib import pyplot as plt
import numpy as np
import math
#import CalcCoeffs 

stuetzstellen = np.linspace(-5, 5, 500)
list_of_functionvalues=[]
list_of_functionvalues.append("Liste")
list_of_functionvalues.append(stuetzstellen)

def a(x):
    return -1*x**2-2*x
def b(x):
    return x**4
def c(x):
    return -1*x**2
output = np.column_stack((stuetzstellen, a(stuetzstellen), b(stuetzstellen), c(stuetzstellen))) #Baut das die arrray untereinander stehen

np.savetxt("Klausurvorbereitung/Output1.txt",output, header="Datei 1")
np.savetxt("Klausurvorbereitung/Output2.txt",(stuetzstellen, a(stuetzstellen), b(stuetzstellen), c(stuetzstellen)), header="Datei 2") #baut die array seitlich zusammen