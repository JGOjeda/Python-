#script para  obtener informacion de tipo serial de un arduino 
import serial
import time 
arduino = serial.Serial('COM5', 115200)
time.sleep(2)
String = arduino.read()
print(serial)
arduino.close()
