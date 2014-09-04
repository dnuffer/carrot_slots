#!/usr/bin/env python
from random import randint
from time import sleep
from os import system
import os.path
from easygui import msgbox

while True:
  delay = randint(60, 2000)
  sleep(delay)
  if os.path.isfile("/usr/share/sounds/GNUstep/Glass.wav"):
    system("aplay /usr/share/sounds/GNUstep/Glass.wav")
  else:
    system("aplay /usr/lib/libreoffice/share/gallery/sounds/kongas.wav")
  msgbox("Hi Dan", "Time is up")
