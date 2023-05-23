#!/usr/bin/env python

import time
import smbus
import struct
import rclpy
import numpy as np
from sensor_msgs.msg import Temperature, Imu
from tf.transformations import quaternion_about_axis
from registers import PWR_MGMT_1, ACCEL_XOUT_H, ACCEL_YOUT_H, ACCEL_ZOUT_H, TEMP_H

ADDR = None
bus = None
IMU_FRAME = None

def read_word(adr):
    high = bus.read_byte_data(ADDR, adr)
    low = bus.read_byte_data(ADDR, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def publish_temp(timer_event):
    temp_msg = Temperature()
    temp_msg.header.frame_id = IMU_FRAME
    temp_msg.temperature = read_word_2c(TEMP_H) / 340.0 + 36.53
    temp_msg.header.stamp = rclpy.time.Time.from_msg(time_msg)
    temp_pub.publish(temp_msg)

def publish_imu(timer_event):
    imu_msg = Imu()
    imu_msg.header.frame_id = IMU_FRAME

    accel_x = read_word_2c(ACCEL_XOUT_H) / 16384.0
    accel_y = read_word_2c(ACCEL_YOUT_H) / 16384.0
    accel_z = read_word_2c(ACCEL_ZOUT_H) / 16384.0
    
    accel = accel_x, accel_y, accel_z
    ref = np.array([0, 0, 1])
    acceln = accel / np.linalg.norm(accel)
    axis = np.cross(acceln, ref)
    angle = np.arccos(np.dot(acceln, ref))
    orientation = quaternion_about_axis(angle, axis)

    gyro_x = read_word_2c(GYRO_XOUT_H) / 131.0
    gyro_y = read_word_2c(GYRO_YOUT_H) / 131.0
    gyro_z = read_word_2c(GYRO_ZOUT_H) / 131.0
    
    o = imu_msg.orientation
    o.x, o.y, o.z, o.w = orientation

    imu_msg.linear_acceleration.x = accel_x
    imu_msg.linear_acceleration.y = accel_y
    imu_msg.linear_acceleration.z = accel_z

    imu_msg.angular_velocity.x = gyro_x
    imu_msg.angular_velocity.y = gyro_y
    imu_msg.angular_velocity.z = gyro_z

    imu_msg.header.stamp = rclpy.time.Time.from_msg(time_msg)

    imu_pub.publish(imu_msg)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('imu_node')

    bus = smbus.SMBus(node.get_parameter('bus').value)
    ADDR = node.get_parameter('device_address').value
    if isinstance(ADDR, str):
        ADDR = int(ADDR, 16)

    IMU_FRAME = node.get_parameter('imu_frame').value

    bus.write_byte_data(ADDR, PWR_MGMT_1, 0)

    temp_pub = node.create_publisher(Temperature, 'temperature', 10)
    imu_pub = node.create_publisher(Imu, 'imu/data', 10)

    imu_timer = node.create_timer(0.02, publish_imu)
    temp_timer = node.create_timer(10, publish_temp)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()