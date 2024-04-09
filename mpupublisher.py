#!/usr/bin/envpython3
import rclpy
from rclpy.node import Node
from my_mpu_package.msg import MPUData
import smbus # subset of l2c but with more functionalities
import time


# sensor register addresses
PWR_MGMT_1 = 0x6B
TEMP_REG_ADDR = 0x41
GYRO_REG_ADDR = 0x43
ACCEL_REG_ADDR = 0x3B

bus = smbus.SMBus(1)

# helper func used tointerpret the 16-bit signed integer data read
# from sensor
def read_word_2c(reg_addr):
    high = bus.read_byte_data(PWR_MGMT_1, reg_addr)
    low = bus.read_byte_data(PWR_MGMT_1, reg_addr+1)
    value = (high << 8) + low
    if (value >= 0x8000):
        return -((65535 - value) + 1)
    else:
        return value
class MPUPublisher(Node):
    def __init__(self):
        super().__init__('mpu_publisher')
        self.publisher = self.create_publisher(MPUData, 'mpu_data', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def read_word_2c(reg_addr):
        high = bus.read_byte_data(PWR_MGMT_1, reg_addr)
        low = bus.read_byte_data(PWR_MGMT_1, reg_addr+1)
        value = (high << 8) + low
        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    def publish_data(self):
        # publish data from sensor
        x_accel, y_accel, z_accel = read_acceleration()
        x_gyro, y_gyro, z_gyro = read_gyroscope()
        temperature = read_temperature()

        msg = MPUData()
        msg.x_accel = x_accel
        msg.y_accel = y_accel
        msg.z_accel = z_accel
        msg.x_gyro = x_gyro
        msg.y_gyro = y_gyro
        msg.z_gyro = z_gyro
        msg.temperature = temperature

        self.publisher.publish(msg)

def read_acceleration():
    accel_x = read_word_2c(ACCEL_REG_ADDR)
    accel_y = read_word_2c(ACCEL_REG_ADDR + 2)
    accel_z = read_word_2c(ACCEL_REG_ADDR + 4)
    return accel_x, accel_y, accel_z

def read_gyroscope():
    gyro_x = read_word_2c(GYRO_REG_ADDR)
    gyro_y = read_word_2c(GYRO_REG_ADDR + 2)
    gyro_z = read_word_2c(GYRO_REG_ADDR + 4)
    return gyro_x, gyro_y, gyro_z

def read_temperature():
    raw_temp = read_word_2c(TEMP_REG_ADDR)
    temperature = (raw_temp / 340.0) + 36.53  # MPU6050 conversion formula
    return temperature

def main(args=None):
    rclpy.init(args=args)
    mpu_publisher = MPUPublisher()
    rclpy.spin(mpu_publisher)
    mpu_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

