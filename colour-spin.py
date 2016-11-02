################################################################################
#
# Bare Conductive Pi Cap
# ----------------------
#
# colour-spin.py - rainbow colours on Pi Cap LED
#
# Written for Raspberry Pi.
#
# Bare Conductive code written by Szymon Kaliski.
#
# This work is licensed under a MIT license https://opensource.org/licenses/MIT
#
# Copyright (c) 2016, Bare Conductive
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#################################################################################

from time import sleep
import signal, sys
import RPi.GPIO as GPIO

red_led_pin = 6
green_led_pin = 5
blue_led_pin = 26

# init GPIO using BCM pinout
# look here for more info on pins: http://pinout.xyz
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up color pins as outputs
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)

def light_rgb(r, g, b):
  # we are inverting the values, because the LED is active LOW
  # LOW - on
  # HIGH - off
  GPIO.output(red_led_pin, not r)
  GPIO.output(green_led_pin, not g)
  GPIO.output(blue_led_pin, not b)

# handle ctrl+c gracefully
def signal_handler(signal, frame):
  light_rgb(0, 0, 0)
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# how long should each colour stay lit before switching to next one
delay_time = 0.5

while True:
  light_rgb(0, 0, 1) # blue
  sleep(delay_time)
  light_rgb(0, 1, 0) # green
  sleep(delay_time)
  light_rgb(1, 0, 0) # red
  sleep(delay_time)
  light_rgb(0, 1, 1) # cyan
  sleep(delay_time)
  light_rgb(1, 1, 0) # yellow
  sleep(delay_time)
  light_rgb(1, 0, 1) # magenta
  sleep(delay_time)
  light_rgb(1, 1, 1) # white
  sleep(delay_time)
  light_rgb(0, 0, 0) # black (off)
  sleep(delay_time)
