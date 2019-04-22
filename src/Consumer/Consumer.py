from src.Configuration.Config import Config
from src.Server.API import API

class Consumer:
    """
    Consumer class to get the message from kafka data pipeline
    """

    def __init__(self):
        """
        Intializes the kakfa consumer
        """
        self.Consumer_Client = Config().setupConsumer()

        if (self.Consumer_Client is False):
            raise TypeError
            exit()


    def __exit__(self):
        """
        Closing producer before class terminates
        """
        try:
            self.Consumer_Client.close()
        except:
            print("Error closing consumer")


    def operate(self):
        """
        Send message to Kafka using Kafka Producer

        :return: Success or failure.
        """
        try:
            api_client = API()
            print('Consumer started')
            while(True):

                for msg in self.Consumer_Client:
                    print(msg.value)
                    api_client.sendData(msg.value)

            return True

        except ValueError:
            print("Value Error while parsing key or messages")
        except ReferenceError:
            print("Producer not available")
            return False
        except TimeoutError:
            print("Timeout error")
            return False