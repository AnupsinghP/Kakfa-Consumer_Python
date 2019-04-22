from src.Settings import settings
from src.Consumer.Consumer import Consumer
import argparse

class ConsumerClient:

    def __init__(self,topic,kafka_server,dataStore,consumerTimeout,server):
        settings['topic'] = topic
        settings['kafka_servers'] = kafka_server
        settings['dataStore'] = dataStore
        settings['consumerTimeout'] = consumerTimeout
        settings['server'] = server
        return

    def main(self):
        """
        Main method for kafka consumer
        :return:
        """
        cons = Consumer()
        cons.operate()


if __name__ == '__main__':
    '''parser = argparse.ArgumentParser(description='Reading from ftp server for family 5N.')
    parser.add_argument('--topic', type=str,
                        help='Topic to read out from',
                        required=True)
    parser.add_argument('--server', type=str,
                        help='Kafak server',
                        required=True)
    parser.add_argument('--dataStore', type=str,
                        help='MongoDb',
                        required=True)
    parser.add_argument('--consumerTimeout', type=int,
                        help='Tim out for consumer',
                        required=True)
    args = parser.parse_args()
    client = ConsumerClient(args.topic, args.server, args.dataStore, args.consumerTimeout)'''
    client = ConsumerClient('first_topic', 'earliest', r"localhost:9092", 1000,r"http://jayglovesdc.com:8080/bny/complaints/create")
    client.main()