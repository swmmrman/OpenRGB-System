#!/bin/env python3
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep

cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
key_name_list = [ key.name[5:] for key in keyboard.leds ]
rows = [
         ['G1', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace',
          'Insert', 'Home', 'Page Up', 'Num Lock', 'Number Pad /', 'Number Pad *', 'Number Pad -'
         ],
         ['G2', 'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\ (ANSI)',
          'Delete', 'End', 'Page Down', 'Number Pad 7', 'Number Pad 8', 'Number Pad 9',
          'Number Pad +'
         ],
         ['G3', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter', 'Number Pad 4',
          'Number Pad 5', 'Number Pad 6'
         ],
       ]

colors = [ RGBColor(255,0,0), RGBColor(0,255,0), RGBColor(0,0,255) ]
i = 0

while True:
  for count, row in enumerate(rows):
    j = i + count
    for key in row:
      keyboard.colors[key_name_list.index(key)] = colors[j % (len(colors)) ]
  keyboard.show()
  i += 1
  sleep(.2)