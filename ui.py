#!/usr/bin/env python

import os
import signal
import sys
from datetime import datetime

# Import only the modules for LCD communication
from library.lcd.lcd_comm_rev_a import LcdCommRevA, Orientation
from library.lcd.lcd_comm_rev_b import LcdCommRevB
from library.lcd.lcd_simulated import LcdSimulated
from library.log import logger

def sighandler(signum, frame):
    global stop
    stop = True

# Set the signal handlers, to send a complete frame to the LCD before exit
signal.signal(signal.SIGINT, sighandler)
signal.signal(signal.SIGTERM, sighandler)
is_posix = os.name == 'posix'
if is_posix:
    signal.signal(signal.SIGQUIT, sighandler)


global lcd_comm

def setup_screen(orientation=Orientation.LANDSCAPE, brightness=15):
    lcd_comm = LcdCommRevA(com_port="AUTO", display_width=320, display_height=480)
    lcd_comm.Reset()
    lcd_comm.InitializeComm()
    
    lcd_comm.SetBrightness(level=brightness)
    
    lcd_comm.SetOrientation(orientation=orientation)
    

def display_text(text="Testing", x=10, y=120):
    lcd_comm.DisplayText(text, x, y,
                         font="roboto/Roboto-Italic.ttf",
                         font_size=20,
                         font_color=(0, 0, 255),
                         background_color=(255, 255, 0),
                         align='right')

def close():
    lcd_comm.closeSerial()

