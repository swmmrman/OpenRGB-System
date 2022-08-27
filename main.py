#!/bin/env python3
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep
import os
import psutil
import signal
import setproctitle

setproctitle.setproctitle("OpenRGB-System")

RUNNING = True

def sig_handler(sig, frame):
  global RUNNING
  RUNNING = False


def get_cpu_sensors():
  sensors = os.listdir("/sys/class/hwmon/")
  for sensor in sensors:
    name = open(F"/sys/class/hwmon/{sensor}/name").readline().strip()
    if name == "coretemp":
      return(F"/sys/class/hwmon/{sensor}/")


BACKGROUND = RGBColor(0x46, 0x25, 0x00)
START_COLOR = RGBColor(0x21, 0x00, 0x00)
KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',]


signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
START_COLORS = keyboard.colors
keyboard.clear()
keyboard.set_color(BACKGROUND)

KEY_NAME_LIST = [ key.name[5:] for key in keyboard.leds ]

cpu_count = psutil.cpu_count()
cpu_sensors = get_cpu_sensors()
print(cpu_sensors)

while RUNNING:
  cpu_usage = psutil.cpu_percent(interval=0.0166, percpu=True)
  for core, percent in enumerate(cpu_usage):
    percent = percent / 100
    key_id = KEY_NAME_LIST.index(KEYS[core].upper())
    keyboard.colors[key_id] = RGBColor(round(percent * 255), 110 - round(percent * 110), 0)

  keyboard.show()

keyboard.colors = START_COLORS
keyboard.show()
print("\r", end="")
