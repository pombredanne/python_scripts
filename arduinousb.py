#!/usr/bin/env python
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    ser.readline()
    print ser.readline()

