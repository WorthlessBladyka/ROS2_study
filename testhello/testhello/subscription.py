#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from std_msgs.msg import String

def listener_callback(msg):
    node.get_logger().info(f'I heard: "{msg.data}"')



def main(args=None):
    global node

    rclpy.init()
    node = rclpy.create_node('sub_hi')
    sub = node.create_subscription(String, 'hi1', listener_callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('shutdown sub!')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()