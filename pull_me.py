#!/usr/bin/env python
from random import randint
from time import sleep
from os import system
from easygui import msgbox

while True:
  sleep(randint(30, 600))
  #for _ in range(5):
  #  print "\a"
  #  time.sleep(.2)
  system("aplay /usr/lib/libreoffice/share/gallery/sounds/kongas.wav")
  msgbox("Hi Dan", "Time is up")
  


