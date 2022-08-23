from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
import random

client = OpenRGBClient()
client.clear()

r = random.Random()

colors = [RGBColor(red=255, green=0, blue=0), RGBColor(red=255, green=122, blue=0), RGBColor(red=0, green=255, blue=0), RGBColor(red=0, green=255, blue=255), RGBColor(red=0, green=0, blue=255), RGBColor(red=255, green=0, blue=255)]

leds = []
for device in client.devices:
  for led in device.leds:
    leds.append(led)

while True:
  r.choice(leds).set_color(r.choice(colors))
