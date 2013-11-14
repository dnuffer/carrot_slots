#!/usr/bin/env python
from random import randint
from time import sleep
from os import system
from easygui import msgbox

while True:
  delay = randint(30, 1100)
  sleep(delay)
  system("aplay /usr/lib/libreoffice/share/gallery/sounds/kongas.wav")
  msgbox("Hi Dan", "Time is up")
