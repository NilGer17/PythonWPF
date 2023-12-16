#!/usr/bin/python3

#print("HEllo world")

"""
Sinnloser Kommentar
print("HEllo world")
print("HEllo world")
print("HEllo world")
"""
#print("HEllo world")

#--------------------
"""
x = 3.1415926/4

sinx = x/1 - (x*x*x)/(3*2*1) + (x*x*x*x*x)/(5*4*3*2*1) 

print ("sin(",x,")=",sinx)
"""
#---------------------
"""
def faculty(n):
    n_fak = 1
    i_n = 1
    while(i_n <=n):
        n_fak = n_fak*i_n
        i_n +=1
    return n_fak    

def sin(x):
    sinx = x/1 - (x**3)/faculty(3) + x**5/faculty(5)
    return sinx

#Hier beginnt Hauptprogramm
x = 3.1415926/4
sinx = sin(x)
print ("sin(",x,")=",sinx)
#---------------------
""" 
"""
#---------------------
def faculty(n):
    n_fak = 1
    i_n = 1
    while(i_n <=n):
        n_fak = n_fak*i_n
        i_n +=1
    return n_fak    

def sin(x):
    exp = 1
    sinx = 0.0
    sign = +1
    while exp<=10:
        sinx = sinx + sign* (x**exp)/faculty(exp)
        exp +=2 
        sign -= sign
    return sinx
#Hier beginnt Hauptprogramm
x = 3.1415926/4
sinx = sin(x)
print ("sin(",x,")=",sinx)
#---------------------
"""
""""
#---------------------
from math import *

def faculty(n):
    n_fak = 1
    i_n = 1
    for i_n in range(1,n+1):
        n_fak = n_fak*i_n
    return n_fak    

def mysin(x):
    exp = 1
    sinx = 0.0
    sign = +1
    for exp in range(1, 17, 2):
        sinx = sinx + sign* (x**exp)/faculty(exp)
       # exp +=2 
        sign -= sign
    return sinx
#Hier beginnt Hauptprogramm
x = pi/4
sinx = mysin(x)
bibsinx = sin(x)

print ("sin(",x,")=",sinx)

print ("bibsin(",x,")=",bibsinx)
#---------------------
"""
#-----------------
""""
import math
import matplotlib.pyplot as plt

dx = 2*math.pi/100

x_list = [i*dx for i in range(0,100)]
y_list = [math.sin(x) for x in x_list]
y2_list = [math.cos(x) for x in x_list]

plt.plot(x_list,y_list, 'black',x_list,y2_list,'r*')
plt.grid()
plt.show()
"""
#-------
""""
dateilesen = open("meinTEXT.txt", "r")
lines = dateilesen.readlines()
list = []
for l in lines:
    #print(l)
    line = l.split(" ")
    #print(line)
    for i in line:
        list.append(float(i))
print(list)

dateilesen.close()

dateischreiben = open("output.txt", "w")
dateischreiben.write(str(list))
"""
#----------
"""
import array as ar
array1 = ar.array()
"""
#----------

import numpy as np
import matplotlib.pyplot as plt
"""
a1 = np.array([1,2,3], np.float64)
a2 = np.array([[11,12,13],[21,22,23],[31,32,33]])
m2 = np.eye((10)) *42  #einheitsmatrix
a3 = np.linspace((0,10),2)
print(a2)
print(a3)
"""
def meineFkt(q):
    return np.sin(q), np.sin(3*q), np.sin(q)**2, (np.sin(10*q)*np.exp(-0.5*q))

Stützstellen = np.linspace(0,2*np.pi, 101)
#print(meineFkt(Stützstellen))
np.savetxt("sinoutData", meineFkt(Stützstellen), "%.15f")


"""
for i in meineFkt(Stützstellen):
    plt.plot(Stützstellen,i)
plt.legend(["sin(x)", "sin(3x)", "sin^2(x)"])
plt.show()
"""
def ichmachNIX():
    pass

