import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self, name):
        super().__init__(name)
        
        self.pub = self.create_publisher(String, "Message1", 10 )
        self.timer = self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        msg = String()
        msg.data = "Hello world test!"
        self.pub.publish(msg)
        self.get_logger().info('Publisher: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode("node1")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()