#!/usr/bin/env python
from random import randint
from time import sleep
from os import system
from easygui import buttonbox

while True:
  choice = buttonbox("Pomodoro", choices = [ "60 min", "15 min", "5 min", "Quit" ])
  if choice != "Quit":
    sleep(int(choice.split(' ')[0]) * 60)
    system("aplay /usr/lib/libreoffice/share/gallery/sounds/kongas.wav")
  else:
    break
