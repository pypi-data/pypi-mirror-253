import logging

from typing import List
from abc import ABC

from kafka import KafkaProducer
from prometheus_client import Counter

from .message import JSONMessage

logger = logging.getLogger(__name__)


class Producer(ABC):

    def __init__(self, producer_settings):
        self.producer = KafkaProducer(**producer_settings)
        self.count_send_msg = Counter('producer_messages_send_total', 'Number of sent messages')

    def send(self, messages: List[JSONMessage]):
        for msg in messages:
            for topic in msg.to_topics:
                self.producer.send(topic=topic, key=msg.key, value=msg.value)
            self.count_send_msg.inc()
        self.producer.flush()
        logger.debug("Flush producer")


class DefaultBatchProducer(Producer):

    def __init__(self, producer_settings):
        self.logger = logging.getLogger(__name__)
        self.producer = KafkaProducer(**producer_settings)

    def send(self, messages: List[JSONMessage]):
        for msg in messages:
            for topic in msg.to_topics:
                self.producer.send(topic=topic, key=msg.key, value=msg.value)
        self.producer.flush()
        self.logger.debug("Flush producer")
