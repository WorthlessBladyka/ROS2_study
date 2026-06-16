#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from std_msgs.msg import String

def hello_callback(message):
    print(f'Received: {message.data}')

def main(args=None):
    # Инициализация ROS2 (без anonymous!)
    rclpy.init(args=args)
    
    # Создаем узел
    node = rclpy.create_node('minimal_subscriber')
    
    # Создаем подписку на топик 'hello'
    subscription = node.create_subscription(
        String,
        'hello',
        hello_callback,
        10  # queue_size
    )
    
    # Держим узел активным
    rclpy.spin(node)
    
    # Очистка (необязательно, но хорошо)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()