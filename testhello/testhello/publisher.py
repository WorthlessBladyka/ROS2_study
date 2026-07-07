import rclpy
from rclpy import node
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("Hello_node")
    top_hi = node.create_publisher(String, 'hi1', 10)
    node.get_logger().info('Node started, publishing to "hello" topic')

    def timer_callback():
        msg = String()
        msg.data = "Hi people"
        top_hi.publish(msg)
        node.get_logger().info(f'top_hi: {msg.data}')

    timer = node.create_timer(0.5, timer_callback)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('shutdown node')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
