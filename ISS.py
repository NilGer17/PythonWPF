#!/usr/bin/python3
import requests
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
import time
from pynput import keyboard
print("ISS Projekt")
def WhereIsISS():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    if response.status_code == 200:
        content = response.json()
        position = content['iss_position']
        lon = float(position["longitude"])
        lat = float(position["latitude"])
        return lon, lat
    else:
        return None
def PrintMap(lon, lat):
        plt.cla()
        WorldMap = Basemap(projection="ortho", lat_0 = lat, lon_0 = lon)
        WorldMap.drawcoastlines()
        WorldMap.drawcountries()
       # WorldMap.fillcontinents()
        #WorldMap.drawrivers()
        wsf_x, wsf_y = WorldMap(11.9, 51.2)
        #iss_x, iss_y = WorldMap(lon_iss, lat_iss)
        WorldMap.plot(wsf_x, wsf_y, "ro", markersize=4)
        #WorldMap.plot(iss_x, iss_y, "ro", markersize=6)
        #plt.show()
        plt.pause(0.01)
class kb_listener_t:    
  # Jede Klasse muss über eine '__init__()'-Methode verfügen.
  # Diese wird von Python automatisch aufgerufen, wenn ein Element
  # vom Typ der Klasse angelegt wird.
  # Die '__' im Namen der Methode haben auch eine Bedeutung...
  def __init__(self):
    # alle Methoden einer Klassen erhalten als ersten Parameter eine Referenz 'self' auf die
    # Instanz der Klasse übergeben. 'self' müssen wir also nicht explizit beim Aufruf einer 
    # Methode angeben. ('self' entspricht in C++ dem 'this'-Zeiger)

    # Objekt zur Aufnahme der Fahrzeug-Steuergrößen v und Lambda
    #self.lon_list = [*range(-360, 720, 1)]
    #self.lat_list = [*range(-90, 90, 1)]
    self.lon = 0
    self.lat = 0

    # Jetzt legen wir eine Instanz des Listener aus dem 'pynput'-Modul an
    self.listener = keyboard.Listener(on_press=self.on_keypress, on_release=self.on_keyrelease)

    self.terminate = False

  # zum Starten des Listeners
  def start_listening(self):
    self.listener.start()

  # zum Stoppen des Listeners
  def stop_listening(self):
    self.listener.stop()

  # Wird bei jedem Tastendruck vom Listener aufgerufen
  # (aber auch entsprechend der Wiederholrate bei gedrückter Taste!)
  def on_keypress(self,key):
   # print('Key pressed: ', key)
    if key == keyboard.Key.right:
      self.lon += 10
      if self.lon > 720:
         self.lon = -360
    elif key == keyboard.Key.left:
      self.lon -= 10
      if self.lon < -360:
         self.lon = 710
    elif key == keyboard.Key.up:
      self.lat += 10
      if self.lat > 90:
         self.lat = -80
    elif key == keyboard.Key.down:
      self.lat -= 10
      if self.lat < -90:
         self.lat = 80
    if key == keyboard.Key.space:
       self.lat = 0
       self.lon = 0
    if key == keyboard.Key.esc:
      self.terminate = True

  # Wird bei jedem Tastenloslassen vom Listener aufgerufen
  def on_keyrelease(self,key):
    #print('Key released: ', key)
    #PrintMap(self.lon, self.lat)
    pass
  def lonlat(self):
     return self.lon, self.lat

if __name__ == "__main__":
   terminated = False
   listner = kb_listener_t()
   listner.start_listening()
   plt.show()
   PrintMap(0,0)

   while not terminated:
      #print("laufe noch...")
      #lon_iss, lat_iss  = WhereIsISS()
      #lon , lat = listner.lonlat()
      #PrintMap(lon, lat, lon_iss, lat_iss)
      #print("Mitte" ,lon, "-", lat)
      terminated = listner.terminate
      #time.sleep(1)