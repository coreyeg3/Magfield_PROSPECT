## This code will collect data from Adafruit LSM303DLHC Magnetometers connected to a RPi via Adafruit TCA9548A multiplexer.
## Data will be collected for each channel listed and written to a txt file as well as uploaded to PROSPECT Slow Control for monitoring
## Author Corey Gilbert
## Last Updated July 15, 2018


import smbus
from influxdb import InfluxDBClient
import time
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8089))

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

n = 5 # number of sensors


def I2C_setup(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)


lsm303 = Adafruit_LSM303.LSM303()
magn = open("mag.txt","a")

## Gain settings for magnetometer +/- 1.9 Gauss
XY_Gain = float(670)
Z_Gain = float(600)

## Channel 0 ##

while True:



	channel = 0
	I2C_setup(mux_channel[channel])
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	# Difference from probe
	X_Cal = 0.112
	Y_Cal = -0.190
	Z_Cal = -0.405

	x = float((mag_x/XY_Gain)+X_Cal)
	y = float((mag_y/XY_Gain)+Y_Cal)
	z = float((mag_z/Z_Gain)+Z_Cal)
	f = math.sqrt((x*x) +(y*y) + (z*z))
	field0 = round(f,3)
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field0)
	s.send("%s" % field0)

## Channel 1 ##

	channel = 1
	I2C_setup(mux_channel[channel])
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	X_Cal = -0.171
	Y_Cal = -0.315
	Z_Cal = -0.511

	x = float((mag_x/XY_Gain)+X_Cal)
	y = float((mag_y/XY_Gain)+Y_Cal)
	z = float((mag_z/Z_Gain)+Z_Cal)
	f = math.sqrt((x*x) +(y*y) + (z*z))
	field1 = round(f,3)
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field1)
	s.send("%s" % field1)

## Channel 2 ##

	channel = 2
	I2C_setup(mux_channel[channel])
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	X_Cal = -0.172
	Y_Cal = 0.255
	Z_Cal = 0.059

	x = float((mag_x/XY_Gain)+X_Cal)
	y = float((mag_y/XY_Gain)+Y_Cal)
	z = float((mag_z/Z_Gain)+Z_Cal)
	f = math.sqrt((x*x) +(y*y) + (z*z))
	field2 = round(f,3)
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field2)
	s.send("%s" % field2)

## Channel 5 ##

	channel = 5
	I2C_setup(mux_channel[channel])
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	X_Cal = 0.258
	Y_Cal = 0.643
	Z_Cal = -0.197

	x = float((mag_x/XY_Gain)+X_Cal)
	y = float((mag_y/XY_Gain)+Y_Cal)
	z = float((mag_z/Z_Gain)+Z_Cal)
	f = math.sqrt((x*x) +(y*y) + (z*z))
	field5 = round(f,3)
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field5)
	s.send("%s" % field5)

## Channel 6 ##

	channel = 6
	I2C_setup(mux_channel[channel])
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	X_Cal = -0.033
	Y_Cal = 0.546
	Z_Cal = -0.023

	x = float((mag_x/XY_Gain)+X_Cal)
	y = float((mag_y/XY_Gain)+Y_Cal)
	z = float((mag_z/Z_Gain)+Z_Cal)
	f = math.sqrt((x*x) +(y*y) + (z*z))
	field6 = round(f,3)
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s \n" % field6)
	s.send("%s" % field6)

	time.sleep(1)





############################################
#Grafana Code
############################################


##json_body = [
##{
##	"measurement": "Magnetic fields",
##	"tags":{
##		"host": "raspberry"
##	},
##	"fields":{
##		"field0": field0,
##		"field1": field1,
##		"field2": field2,
##		"field5": field5,
##		"field6": field6
##		}
##}
##]
##client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
##client.switch_database('mydb')
##client.write_points(json_body)
##magn.close()