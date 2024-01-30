## KAFKA-CLIENT-NEW

### Примеры использования:

### Через manager

```python
import json
import logging

from kafka_client import (
    DefaultBatchKafkaManager, 
    DefaultBatchProducer, 
    DefaultBatchConsumer,
)
from kafka_client.handler import EmptyHandler

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    batch_size = 10
    consumer_settings = {
        'bootstrap_servers': '...',
        'value_deserializer': lambda v: json.loads(v.decode('utf-8')),
        'key_deserializer': lambda k: k.decode('utf-8'),
        'client_id': '...',
        'group_id': '...',
        'enable_auto_commit': False,
        'auto_offset_reset': 'earliest'
    }
    consumer = DefaultBatchConsumer(
        topic='...',
        batch_size=batch_size,
        consumer_settings=consumer_settings
    )
    
    producer_settings = {
        'bootstrap_servers': '...',
        'key_serializer': str.encode,
        'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    }
    producer = DefaultBatchProducer(topic='...', producer_settings=producer_settings)
    
    manager = DefaultBatchKafkaManager(consumer, producer)
    manager.set_handler(handler=EmptyHandler())
    manager.run()
```

#### Через функцию run

задаем переменные окружения


 - `BATCH_SIZE` [optional] - размер батча
 - `BOOTSTRAP_SERVERS` - брокеры кафки
 - `INPUT_TOPIC` - входной топик
 - `OUTPUT_TOPIC` - выходной топик
 - `CLIENT_ID` [optional] - имя приложения, как то отсылается в кафку
 - `GROUP_ID` - kafka consumer group

Запускаем `python`:

```python
import logging

from kafka_client import run
from kafka_client.handler import EmptyHandler

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    run(handler=EmptyHandler())
```