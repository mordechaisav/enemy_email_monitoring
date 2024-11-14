"""'Identifying suspicious content:
The code will listen to every incoming message. If a message contains suspicious content such as "hostage" or "explos", it will be routed
(messages.explosive or messages.hostage) are suitable for Kafka topics'"""
import json

from kafka import KafkaConsumer,KafkaProducer


consumer = KafkaConsumer(
    'messages_all',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    group_id='read_all_emails',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def is_suspicious(message):
    suspicious_words = ['hostage', 'explos']
    return any(word in message.lower() for word in suspicious_words)


for message in consumer:
    if is_suspicious(message.value['content']):
        producer.send('messages.explosive', message.value)
        producer.send('messages.hostage', message.value)
    print(f"Received message: {message.value}")
