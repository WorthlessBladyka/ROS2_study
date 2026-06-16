#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('hello_topic_publisher')
    
    publisher = node.create_publisher(String, 'hello', 10)
    node.get_logger().info('Node started, publishing to "hello" topic')
    
    # Создаем таймер для публикации с частотой 10 Гц
    def timer_callback():
        msg = String()
        msg.data = 'hello world!'
        publisher.publish(msg)
        node.get_logger().info(f'Published: {msg.data}')
    
    timer = node.create_timer(0.1, timer_callback)  # 0.1 сек = 10 Гц
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()