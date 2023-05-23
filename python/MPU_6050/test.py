from mpu6050 import mpu6050
from time import sleep
import os
import math
from math import sqrt, atan, atan2, pi

sensor = mpu6050(0x68)

while True:
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()
    
    RateRoll=gyro_data['x']/65.5
    RatePitch=gyro_data['y']/65.5
    RateYaw=gyro_data['z']/65.5
    
    AngleRoll = (atan(accel_data['y']/sqrt(accel_data['x']*accel_data['x']+accel_data['z']*accel_data['z'])))*1/(pi/180)
    AnglePitch = (atan(accel_data['x']/sqrt(accel_data['y']*accel_data['y']+accel_data['z']*accel_data['z'])))*1/(pi/180)
    AngleYaw = (atan2(accel_data['x'], accel_data['y']))*1/(pi/180)
    
    
    print("Rate Roll", RateRoll)
    print("Rate Pitch", RatePitch)
    print("Rate Yaw", RateYaw)
    print("")
    print("AngleRoll", AngleRoll)
    print("AnglePitch", AnglePitch)
    print("AngleYaw", AngleYaw)
    
    """
    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))

    print("Temp: " + str(temp) + " C")
    """
    
    
    sleep(0.1)
    os.system('clear')
    
