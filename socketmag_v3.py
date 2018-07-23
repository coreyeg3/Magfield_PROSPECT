## This code will collect data from Adafruit LSM303DLHC Magnetometers connected to a RPi via Adafruit TCA9548A multiplexer.
## Data will be collected for each channel listed and written to a txt file as well as uploaded to PROSPECT Slow Control for monitoring
## Author Corey Gilbert
## Last Updated July 23, 2018


import smbus
from influxdb import InfluxDBClient
import time
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math
import socket
import sys

#####################################################
#Socket Connection
#####################################################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.16.10.1', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

sock.bind(server_address)

#####################################################
#Multiplexer Addessring
#####################################################

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
magn = open("mag.txt","a")

## Gain settings for magnetometer +/- 1.9 Gauss
XY_Gain = float(670)
Z_Gain = float(600)

sock.listen(1)

## Channel 0 ##

while True:

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
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field0)


## Channel 1 ##

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
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field1)


## Channel 2 ##

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
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field2)


## Channel 5 ##

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
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field5)


## Channel 6 ##

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
	magn.write("%s," % x)
	magn.write("%s," % y)
	magn.write("%s," % z)
	magn.write("%s," % field6)


## Channel 7 ##

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
    magn.write("%s," % x)
    magn.write("%s," % y)
    magn.write("%s," % z)
    magn.write("%s \n" % field7)



############################################
# Socket listen/send data upon request
############################################
    while True:
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print >>sys.stderr, 'connection from', client_address
            field0 = str(field0)
            field1 = str(field1)
            field2 = str(field2)
            field5 = str(field5)
            field6 = str(field6)
            field7 = str(field7)
            connection.sendall(field0)
            connection.sendall(field1)
            connection.sendall(field2)
            connection.sendall(field5)
            connection.sendall(field6)
            connection.sendall(field7)
        finally:
            connection.close()
    time.sleep(0.5)


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




