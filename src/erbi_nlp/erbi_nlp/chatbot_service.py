import rclpy
from rclpy.node import Node
from erbi_base.srv import Conversation
from chatbot.chatbot import Chatbot

class ChatBot(Node):

    def __init__(self):
        super().__init__('ChatBot')
        self.get_logger().info('ChatBot node started')
        self.srv = self.create_service(Conversation, 'conversation', self.conversation_callback)
        self.agent = Chatbot()

    def conversation_callback(self, request, response):
        response.result = self.agent.response(request.question)

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = ChatBot()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()