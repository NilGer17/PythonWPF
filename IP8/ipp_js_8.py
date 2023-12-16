#!/usr/bin/python3
"""
IPP - Ingenieurwissenschaftliches Programmieren mit Python
Aufgabe A_js_8_1 

- Hauptprogramm unter Nutzung von pygame mit Event-Logik
- Einlesen Lambda und v von der Tastatur oder via Joystick

(c) Prof. Dr.-Ing. Volker von Holt / Fahrzeuginformatik
"""

# Importieren der Pygame-Bibliothek
import sys
import pygame
from pygame.locals import *

import os

# HIER: Simulationsmodul importieren
#import ipp_8_1_template as ipp_8
#import ipp_8_1_2 as ipp_8
#import ipp_8_2 as ipp_8
#import ipp_8_3 as ipp_8
import ipp_8_4 as ipp_8

import kb_listener

import ipp_8_config as cfg

# Events von Maus, Tastatur und Joystick bekommt standardmäßig immer nur das Fenster, 
# das den Fokus hat. Lässt sich aber ändern...
# Joystick-Events auch ohne Fokus erhalten
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"


JS_AXIS_V = 4
JS_AXIS_LAMBDA = 0

#JS_AXIS_V = int(cfg.joystick['axis_v'])
#JS_AXIS_LAMBDA = int(cfg.joystick['axis_Lambda'])

#-------------------------------------------------------------------------------
# Klasse zur Behandlung von Joystick-/Gamepad-Events
class joystick_handler(object):
  def __init__(self, id):
    self.id = id
    self.joy = pygame.joystick.Joystick(id)
    self.name = self.joy.get_name()
    self.joy.init()
    self.numaxes    = self.joy.get_numaxes()
    self.numballs   = self.joy.get_numballs()
    self.numbuttons = self.joy.get_numbuttons()
    self.numhats    = self.joy.get_numhats()

    self.axis = []
    for i in range(self.numaxes):
      self.axis.append(self.joy.get_axis(i))

    self.ball = []
    for i in range(self.numballs):
      self.ball.append(self.joy.get_ball(i))

    self.button = []
    for i in range(self.numbuttons):
      self.button.append(self.joy.get_button(i))

    self.hat = []
    for i in range(self.numhats):
      self.hat.append(self.joy.get_hat(i))
#-------------------------------------------------------------------------------
# Hauptprogramm: Einstiegspunkt
if __name__ == '__main__':

  # initialisieren von pygame
  pygame.init()

  # einige Events interessieren uns einfach nicht
  pygame.event.set_blocked((MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN))

  # genutzte Farbe
  ORANGE  = ( 255, 140, 0)
  ROT     = ( 255, 0, 0)
  GRUEN   = ( 0, 255, 0)
  SCHWARZ = ( 0, 0, 0)
  WEISS   = ( 255, 255, 255)

  # HIER: Simulation instanziieren
  drive_sim = ipp_8.drive_sim_t()
  
  vehicle_ctrl = kb_listener.vehicle_ctrl_t()

  # Fenster öffnen
  #screen = pygame.display.set_mode((640, 480),flags=pygame.HIDDEN)
  screen = pygame.display.set_mode((160, 120))

  # Titel für Fensterkopf
  pygame.display.set_caption("Drive-Sim-Game")

  # solange die Variable False ist, soll das Spiel laufen
  terminated = False

  # Joysticks initialisieren
  joycount = pygame.joystick.get_count()
  if joycount == 0:
    print("This program only works with at least one joystick plugged in. No joysticks were detected.")
  joy = []
  for i_joy in range(joycount):
      joy.append(joystick_handler(i_joy))
  print(joycount, ' Joystick(s) gefunden')

  # Bildschirm Aktualisierungen einstellen
  clock = pygame.time.Clock()

  # Spielfeld löschen
  screen.fill(WEISS)

  # Spielfeld/-figuren zeichnen

  # Fenster aktualisieren
  pygame.display.flip()

  # unterdrücken der Textmeldungen zu den Events
  silent_mode = False #True

  # Schleife Hauptprogramm
  while not terminated:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        if not silent_mode:
          print("QUIT-Button clicked")
        terminated = True

      elif event.type == pygame.KEYDOWN:
        if not silent_mode:
          print("KEY pressed")

        if event.key == pygame.K_ESCAPE:
          if not silent_mode:
            print("ESC-KEY pressed")
          terminated = True

        elif event.key == pygame.K_RIGHT:
          if not silent_mode:
            print("ARROW-RIGHT-KEY pressed")
          vehicle_ctrl.set_Lambda_inc(-1)

        elif event.key == pygame.K_LEFT:
          if not silent_mode:
            print("ARROW-LEFT-KEY pressed")
          vehicle_ctrl.set_Lambda_inc(+1)

        elif event.key == pygame.K_UP:
          if not silent_mode:
            print("ARROW-UP-KEY pressed")
          vehicle_ctrl.set_v_inc(+1)

        elif event.key == pygame.K_DOWN:
          if not silent_mode:
            print("ARROW-DOWN-KEY pressed")
          vehicle_ctrl.set_v_inc(-1)

        elif event.key == pygame.K_SPACE:
          if not silent_mode:
            print("SPACE-KEY pressed")

      elif event.type == pygame.MOUSEBUTTONDOWN:
        if not silent_mode:
          print("MOUSE clicked")

      elif event.type == JOYAXISMOTION:
        joy[event.joy].axis[event.axis] = event.value
        if not silent_mode:
          print('JS-AXIS[',event.axis,']= ', event.value)

        if event.axis == JS_AXIS_V:
          if event.value < 0:
            vehicle_ctrl.set_v(-event.value)
          """
          if event.value < 0:
            vehicle_ctrl.set_v_inc(+0.01)
          elif event.value > 0:
            vehicle_ctrl.set_v_inc(-0.01)
          """

        if event.axis == JS_AXIS_LAMBDA:
          vehicle_ctrl.set_Lambda(-event.value)
          """
          if event.value < 0:
            vehicle_ctrl.set_Lambda_inc(+0.1)
          elif event.value > 0:
            vehicle_ctrl.set_Lambda_inc(-0.1)
          """

      elif event.type == JOYBALLMOTION:
        joy[event.joy].ball[event.ball] = event.rel
        if not silent_mode:
          print("JS-BALL moved")

      elif event.type == JOYHATMOTION:
        joy[event.joy].hat[event.hat] = event.value
        if not silent_mode:
          print("JS-HAT moved")

      elif event.type == JOYBUTTONUP:
        joy[event.joy].button[event.button] = 0
        if not silent_mode:
          print("JS-BUTTON released")

      elif event.type == JOYBUTTONDOWN:
        joy[event.joy].button[event.button] = 1
        if not silent_mode:
          print("JS-BUTTON pressed")

    # Spiellogik hier integrieren
    # HIER: Simlation für einen Durchlauf aufrufen
    if not terminated:
      terminated = drive_sim.run(vehicle_ctrl.v,vehicle_ctrl.Lambda)

    # Spielfeld löschen
    screen.fill(WEISS)

    # Spielfeld/figuren zeichnen

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen [ms]
    clock.tick(100)

  pygame.quit()
#-------------------------------------------------------------------------------
