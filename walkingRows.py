#!/bin/env python3
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep
import signal

RUNNING = True

def sig_handler(sig, frame):
  global RUNNING
  RUNNING = False


signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
keyboard.clear()
key_name_list = [ key.name[5:] for key in keyboard.leds ]
rows = [
         ['', 'Brightness'], # '' = Logo
         ['Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
          'Print Screen', 'Scroll Lock', 'Pause/Break', 'Media Previous', 'Media Play/Pause',
          'Media Next', 'Media Mute'
         ],
         ['G1', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace',
          'Insert', 'Home', 'Page Up', 'Num Lock', 'Number Pad /', 'Number Pad *', 'Number Pad -'
         ],
         ['G2', 'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\ (ANSI)',
          'Delete', 'End', 'Page Down', 'Number Pad 7', 'Number Pad 8', 'Number Pad 9',
          'Number Pad +'
         ],
         ['G3', 'Caps Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter',
          'Number Pad 4', 'Number Pad 5', 'Number Pad 6'
         ],
         ['G4', 'Left Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Right Shift',
          'Up Arrow', 'Number Pad 1', 'Number Pad 2', 'Number Pad 3', 'Number Pad Enter'
         ],
         ['G5', 'Left Control', 'Left Windows', 'Left Alt', 'Space', 'Right Windows', 'Menu',
          'Right Control', 'Left Arrow', 'Down Arrow', 'Right Arrow', 'Number Pad 0', 'Number Pad .'
         ]
       ]

colors = [ RGBColor(255,0,0), RGBColor(0,255,0), RGBColor(0,0,255) ]
i = 0

while RUNNING:
  for count, row in enumerate(rows):
    j = i + count
    for key in row:
      keyboard.colors[key_name_list.index(key)] = colors[j % (len(colors)) ]
  keyboard.show()
  i += 1
  sleep(.25)
