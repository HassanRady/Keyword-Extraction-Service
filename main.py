from kafka import KafkaProducer, KafkaConsumer

from config import settings
from keywords_extractor import pipeline

import json

producer = KafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

consumer = KafkaConsumer(settings.KAFKA_CLEANED_TEXT_TOPIC,
                         bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                         auto_offset_reset='latest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

try:
    while True:
        for message in consumer:
            data = message.value
            keywords = pipeline(data['text'])
            if not keywords['output']:
                continue
            producer.send(settings.KAFKA_KEYWORDS_TOPIC, keywords)
finally:
    producer.close()
    consumer.close()
