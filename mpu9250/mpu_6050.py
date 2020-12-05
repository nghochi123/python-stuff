from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)
pa = {'x': 0, 'y':0, 'z':0}
pg = {'x': 0, 'y':0, 'z':0}

'''
This is for making the acceleration data as well as the gyro data only show
something when there is a change.
'''

while True:
    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']-pa['x']))
    print("Acc Y : "+str(accel_data['y']-pa['y']))
    print("Acc Z : "+str(accel_data['z']-pa['z']))
    print()
    pa = accel_data.copy()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']-pg['x']))
    print("Gyro Y : "+str(gyro_data['y']-pg['y']))
    print("Gyro Z : "+str(gyro_data['z']-pg['z']))
    print()
    pg = gyro_data.copy()
    print("-------------------------------")
    time.sleep(1)
