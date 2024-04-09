#!/usr/bin/envpython3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class MPUSubscriber(Node):
    def __init__(self):
        super().__init__('mpu_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'mpu_data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        '''extracts sens data from pub then logs to console'''
        temperature = msg.data[0]
        gyro_x = msg.data[1]
        gyro_y = msg.data[2]
        gyro_z = msg.data[3]
        accel_x = msg.data[4]
        accel_y = msg.data[5]
        accel_z = msg.data[6]

        self.get_logger().info(
            'Temperature: {:.2f}°C, Gyro (X,Y,Z): {:.2f}, {:.2f}, {:.2f}, Acceleration (X,Y,Z): {:.2f}, {:.2f}, {:.2f}'.format(
                temperature, gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z))

def main(args=None):
    rclpy.init(args=args)
    mpu_subscriber = MPUSubscriber()
    rclpy.spin(mpu_subscriber)
    mpu_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

