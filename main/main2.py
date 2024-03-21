from kafka import KafkaConsumer
from pymongo import MongoClient
import json


class MessageConsumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.consumer = KafkaConsumer(
            topic,  # Topic to consume
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode(
                "utf-8"
            ),  # Decode message value as utf-8
            group_id="my-group",  # Consumer group ID
            auto_offset_reset="earliest",  # Start consuming from earliest available message
            enable_auto_commit=True,  # Commit offsets automatically
        )

    def receive_message(self):
        try:
            for message in self.consumer:
                # 데이터를 MongoDB에 저장
                self.save_to_mongodb(json.loads(message.value))
                print("Data saved ro MongoDB: ", message.value)
        except Exception as exc:
            raise exc
        
    
    def save_to_mongodb(self, data):
        client = MongoClient('localhost', 27017)
        db = client['mydatabase']
        collection = db['collection_name']
        collection.insert_one(data)

broker = ["localhost:9094"]
topic = "my-topic"

cs = MessageConsumer(broker, topic)
cs.receive_message()

