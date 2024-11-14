import json

from kafka import KafkaConsumer,KafkaProducer


consumer = KafkaConsumer(
    'message_all',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='read_all_emails',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def is_hostage(message):
    for sentence in message:
        if 'hostage' in sentence.lower():
            return True
def is_explos(message):
    for sentence in message:
        if 'explos' in sentence.lower():
            return True

for message in consumer:
    if is_explos(message.value['sentence']):
        producer.send('messages.explosive', message.value)
    if is_hostage(message.value['sentence']):
        producer.send('messages.hostage', message.value)
    print(f"Received message: {message.value}")
