from kafka import KafkaConsumer

class Config:
    """
    Configuration for the Kafka consumer.
    """

    def setupConsumer(self):
        """
        Setup kafka producer for sending messages to Kafka.
        :return:
        """
        try:
            consumer = KafkaConsumer('first_topic', auto_offset_reset='latest',
                                     bootstrap_servers=['localhost:9092'],
                                     consumer_timeout_ms=1000)

            return consumer

        except ConnectionError as e:
            print("Error creating Kakfka Consumer")
            return False