#!/bin/env python3
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from time import sleep
import psutil
import signal

RUNNING = True

def sig_handler(sig, frame):
  global RUNNING
  RUNNING = False


BACKGROUND = RGBColor(0x46, 0x25, 0x00)
START_COLOR = RGBColor(0x21, 0x00, 0x00)
KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',]


signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

cli = OpenRGBClient()
keyboard = cli.get_devices_by_type(DeviceType.KEYBOARD)[0]
keyboard.clear()
key_name_list = [ key.name[5:] for key in keyboard.leds ]


cpu_count = psutil.cpu_count()
