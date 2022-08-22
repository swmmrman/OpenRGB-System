#!/usr/bin/env python3

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep

client = OpenRGBClient()

keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0]
keys = keyboard.zones[0].leds

for key in keys:
  key.set_color(RGBColor(225,0,0))
  sleep(.1)
  
