from kafka import KafkaProducer
import json

from kafka_files.produser.mongoDB import collection

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
def get_message(data):
    collection.insert_one(data)
    producer.send('messages_all', str(data))
    print(f'Message sent: {data}')
    return data

