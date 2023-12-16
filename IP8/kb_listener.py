#!/usr/bin/python3
"""
IPP - Ingenieurwissenschaftliches Programmieren mit Python
# kb_listener

Klasse zum Mithören der Tastatur und zur Anpassung von v und Lambda

(c) Prof. Dr.-Ing. Volker von Holt / Fahrzeuginformatik
"""
# Importieren der notwendigen Module
from pynput.keyboard import Listener
from pynput import keyboard

#-------------------------------------------------------------------------------
# Klasse zur Aufnahme aller simulations-/fahrzeugspezifischen Attribute 
# und Methoden
class vehicle_ctrl_t:
  #-------------------------------------
  # Konstruktor
  def __init__(self):
    self.v = 0.0        # aktuelles v_soll
    self.Lambda = 0.0   # aktuelles Lambda_soll

    # Jetzt legen wir noch die Inkremente für v und Lambda fest ...
    self.v_inc = 0.5        # in [m/s]
    self.Lambda_inc = 0.01  # in [rad]

    # ... und die oberen und unteren Grenzen
    self.v_lower_bound =  0.0   # Rückwärtsfahren geht erst einmal nicht
    self.v_upper_bound = 30.0   # ca. 110 km/h
    self.Lambda_lower_bound = -0.75 #-0.75   # ca. -PI/4 = -45 Grad
    self.Lambda_upper_bound = +0.75 #+0.75   # ca. +PI/4 = +45 Grad
  #-------------------------------------
  # Methode zum inkrementellen Erhöhen/Vermindern von v
  # inc_dir: +1 => v um ein Inkrement erhöhen
  # inc_dir: -1 => v um ein Inkrement vermindern
  def set_v_inc(self,inc_dir):
    # - Berechnen des resultierenden v
    self.v = self.v + inc_dir*self.v_inc
    # - Prüfung auf Einhaltung der oberen/unteren Grenze
    self.v = max(min(self.v,self.v_upper_bound),self.v_lower_bound)
  #-------------------------------------
  # Methode zum inkrementellen Erhöhen/Vermindern von Lambda
  # inc_dir: +1 => Lambda um ein Inkrement erhöhen
  # inc_dir: -1 => Lambda um ein Inkrement vermindern
  def set_Lambda_inc(self,inc_dir):
    # - Berechnen des resultierenden Lambda
    self.Lambda = self.Lambda + inc_dir*self.Lambda_inc
    # - Prüfung auf Einhaltung der oberen/unteren Grenze
    self.Lambda = max(min(self.Lambda,self.Lambda_upper_bound),self.Lambda_lower_bound)
  #-------------------------------------
  # Methode zum direkten Setzen eines neuen Wertes für v
  # value: 0..1 gibt v bezogen auf das Intervall "upper_bound - lower_bound" an
  # (Methode kommt zusammen mit dem Gamepad zum Einsatz)
  def set_v(self,value):
    # - Prüfen auf korrekten Wertebereich von value
    if value < 0.0 or value > 1.0:
      print('Wertebereich v')
      return
    # - Berechnen des resultierenden v
    if value > 0:
      self.v = (self.v_upper_bound-self.v_lower_bound) * value
  #-------------------------------------
  # Methode zum direkten Setzen eines neuen Wertes für Lambda
  # value: 0..1 gibt Lambda bezogen auf das Intervall "upper_bound - lower_bound" an
  # (Methode kommt zusammen mit dem Gamepad zum Einsatz)
  def set_Lambda(self,value):
    # - Prüfen auf korrekten Wertebereich von value
    if value < -1.0 or value > +1.0:
      print('Wertebereich Lambda')
      return
    # - Berechnen des resultierenden Lambda
    if value > 0.0:
      self.Lambda = (+self.Lambda_upper_bound) * value
    else:
      self.Lambda = (-self.Lambda_lower_bound) * value

    
"""
Hier definieren wir eine Klasse für das Abfangen der Tastenbetätigung
"""
# ... das "angehängte" '_t' am Klassennamen soll ausdrücken, dass es sich bei dem Bezeichner
# nicht um eine Datenelement, sondern um eine Typdefinition handelt.
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
    self.vehicle_ctrl = vehicle_ctrl_t()

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
    #print('Key pressed: ', key)
    if key == keyboard.Key.up:
      self.vehicle_ctrl.set_v_inc(+1)
    elif key == keyboard.Key.down:
      self.vehicle_ctrl.set_v_inc(-1)
    elif key == keyboard.Key.right:
      self.vehicle_ctrl.set_Lambda_inc(-1)
    elif key == keyboard.Key.left:
      self.vehicle_ctrl.set_Lambda_inc(+1)

    if key == keyboard.Key.esc:
      self.terminate = True

  # Wird bei jedem Tastenloslassen vom Listener aufgerufen
  def on_keyrelease(self,key):
    #print('Key released: ', key)
    pass

