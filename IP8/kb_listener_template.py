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
    # ToDo: Definieren und Initialisieren aller Attribute
    pass
  #-------------------------------------
  # Methode zum inkrementellen Erhöhen/Vermindern von v
  # inc_dir: +1 => v um ein Inkrement erhöhen
  # inc_dir: -1 => v um ein Inkrement vermindern
  def set_v_inc(self,inc_dir):
    # ToDo: 
    # - Berechnen des resultierenden v
    # - Prüfung auf Einhaltung der oberen/unteren Grenze
    pass
  #-------------------------------------
  # Methode zum inkrementellen Erhöhen/Vermindern von Lambda
  # inc_dir: +1 => Lambda um ein Inkrement erhöhen
  # inc_dir: -1 => Lambda um ein Inkrement vermindern
  def set_Lambda_inc(self,inc_dir):
    # ToDo: 
    # - Berechnen des resultierenden Lambda
    # - Prüfung auf Einhaltung der oberen/unteren Grenze
    pass
  #-------------------------------------
  # Methode zum direkten Setzen eines neuen Wertes für v
  # value: 0..1 gibt v bezogen auf das Intervall "upper_bound - lower_bound" an
  # (Methode kommt zusammen mit dem Gamepad zum Einsatz)
  def set_v(self,value):
    # ToDo: 
    # - Prüfen auf korrekten Wertebereich von value
    # - Berechnen des resultierenden v
    pass
  #-------------------------------------
  # Methode zum direkten Setzen eines neuen Wertes für Lambda
  # value: 0..1 gibt v bezogen auf das Intervall "upper_bound - lower_bound" an
  # (Methode kommt zusammen mit dem Gamepad zum Einsatz)
  def set_Lambda(self,value):
    # ToDo: 
    # - Prüfen auf korrekten Wertebereich von value
    # - Berechnen des resultierenden Lambda
    pass
    
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

