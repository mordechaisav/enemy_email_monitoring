import json
from kafka_files.produser.mongoDB import collection
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'messages_all',
    bootstrap_servers='localhost:9092',  # broker
    group_id='group_message_all',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    print(msg)
    collection.insert_one(msg.value)
    consumer.commit()


