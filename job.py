from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': 'kafka:9092',
        'client.id': socket.gethostname()}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

topic = "test-kafka-topic"

producer.produce(topic, key='key', value='Hello from Flink producer!', callback=delivery_report)

producer.flush()