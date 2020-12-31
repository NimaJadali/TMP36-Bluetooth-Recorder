import serial
import time
import numpy as np

print("start")
port="COM12"
serial_speed = 9600
serial_port = 'COM12'
bluetooth = serial.Serial(serial_port, serial_speed)
print("connected")
bluetooth.flushInput()

temperatureArray = np.zeros((2400,))
for i in range(2400):
    read_bytes = bluetooth.readline()
    print(float(read_bytes))
    temperatureArray[i] = (float(read_bytes))
    time.sleep(1)

temperatureArray = temperatureArray.reshape((240, 10))
print(temperatureArray)
np.save('secondTest', temperatureArray)

tempsAverage = [np.mean(temps) for temps in temperatureArray]
print(tempsAverage)
np.save('secondTestAverages', tempsAverage)