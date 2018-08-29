"""
 This code will collect data from Adafruit LSM303DLHC Magnetometers connected to a RPi via Adafruit TCA9548A multiplexer.
 Data will be collected for each channel listed and written to a txt file in 1 second intervals.
 Seperate file for averaging data will be run for selected intervals. 
 Author Corey Gilbert
 Last Updated July 31, 2018
"""

## Server
## interrupt when connection
## wait for connection to come,
## file decription will come from orca and I send back
## memory map io
## mmap python function

import smbus
import time
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math
import sys
import os

########################
#Multiplexer Addessring
########################

I2C_address = 0x70
I2C_bus_number = 1
I2C_ch_0 = 0b00000001
I2C_ch_1 = 0b00000010
I2C_ch_2 = 0b00000100
I2C_ch_3 = 0b00001000
I2C_ch_4 = 0b00010000
I2C_ch_5 = 0b00100000
I2C_ch_6 = 0b01000000
I2C_ch_7 = 0b10000000

mux_channel = [I2C_ch_0, I2C_ch_1, I2C_ch_2, I2C_ch_3, I2C_ch_4, I2C_ch_5, I2C_ch_6, I2C_ch_7]

#n = 5 # number of sensors


def I2C_setup(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)


lsm303 = Adafruit_LSM303.LSM303()
magn = open("mag.txt","ax+")

## Gain settings for magnetometer +/- 1.9 Gauss
XY_Gain = float(670)
Z_Gain = float(600)

averagingtime = 10 #Minutes

## Channel 0 ##

while True:
	execfile('multisetup.py')
	t_end = time.time() + 60 * averagingtime
	while time.time() < t_end:
		data = open("data.txt","ax+") ## file to be opened for averaging
		
		## Channel 0 ##
		try:
			channel = 0
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			# Difference from probe
			X_Cal = 1.349
			Y_Cal = -0.017
			Z_Cal = -1.102

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field0 = round(f,3)
			data.write("%s," % field0)
		except IOError:
			data.write("0.000,")
			pass

	## Channel 1 ##
		try:
			channel = 1
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			X_Cal = 0.056
			Y_Cal = -1.819
			Z_Cal = -1.815

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field1 = round(f,3)
			data.write("%s," % field1)
		except IOError:
			data.write("0.000,")
			pass

	## Channel 2 ##
		try:
			channel = 2
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			X_Cal = 1.479
			Y_Cal = -0.350
			Z_Cal = -0.836

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field2 = round(f,3)
			data.write("%s," % field2)
		except IOError:
			data.write("0.000,")
			pass

	## Channel 5 ##
		try:
			channel = 5
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			X_Cal = 1.179
			Y_Cal = -0.906
			Z_Cal = -1.610

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field5 = round(f,3)
			data.write("%s," % field5)
		except IOError:
			data.write("0.000,")
			pass

	## Channel 6 ##
		try:
			channel = 6
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			X_Cal = 1.971
			Y_Cal = -0.142
			Z_Cal = -1.185

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field6 = round(f,3)
			data.write("%s," % field6)
		except IOError:
			data.write("0.000,")
			pass

	## Channel 7 ##
		try:
			channel = 7
			I2C_setup(mux_channel[channel])
			accel, mag = lsm303.read()
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			X_Cal = 2.183
			Y_Cal = -1.122
			Z_Cal = -1.348

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field7 = round(f,3)
			data.write("%s \n" % field7)
		except IOError:
			data.write("0.000 \n")
			pass
		
		time.sleep(1) ## Sample data every 1 second
	
	
	execfile(avg.py)

	






