#!/usr/bin/env python3

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep

client = OpenRGBClient()
client.clear()

keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0]
keys = keyboard.zones[0].leds

razer = client.get_devices_by_type(DeviceType.LEDSTRIP)[0]
#Skiping zones 0 and 2 as nothing is connected right now

razer.leds = [razer.zones[1].leds, razer.zones[3].leds, razer.zones[4].leds, razer.zones[5].leds]
fan_leds = [led for sublist in razer.leds for led in sublist]

for key in keys:
  key.set_color(RGBColor(225,0,0))
  sleep(.1)

for led in fan_leds:
  led.set_color(RGBColor(0,0,255))
  sleep(.1)
