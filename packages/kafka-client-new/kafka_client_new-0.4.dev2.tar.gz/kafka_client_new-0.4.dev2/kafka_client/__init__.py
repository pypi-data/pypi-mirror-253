from .consumer import KafkaConsumer, DefaultBatchConsumer, MultiTopicBatchConsumer
from .producer import KafkaProducer, DefaultBatchProducer
from .manager import KafkaManager, DefaultBatchKafkaManager, RoutingBatchManager
from .handler import Handler
from .message import JSONMessage

from .__version__ import version


def run(handler: Handler):
    import json
    import os

    batch_size = os.getenv('BATCH_SIZE', 100)
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    input_topic = os.getenv('INPUT_TOPIC')
    output_topic = os.getenv('OUTPUT_TOPIC')
    client_id = os.getenv('CLIENT_ID', 'transformer')
    group_id = os.getenv('GROUP_ID')

    consumer_settings = {
        'bootstrap_servers': bootstrap_servers,
        'value_deserializer': lambda v: json.loads(v.decode('utf-8')),
        'key_deserializer': lambda k: k.decode('utf-8'),
        'client_id': client_id,
        'group_id': group_id,
        'enable_auto_commit': False,
        'auto_offset_reset': 'earliest',
    }
    consumer = DefaultBatchConsumer(
        topic=input_topic, consumer_settings=consumer_settings
    )

    producer_settings = {
        'bootstrap_servers': bootstrap_servers,
        'key_serializer': str.encode,
        'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    }
    producer = DefaultBatchProducer(
        producer_settings=producer_settings
    )

    manager = DefaultBatchKafkaManager(consumer, producer)
    manager.set_handler(handler)

    manager.run()
