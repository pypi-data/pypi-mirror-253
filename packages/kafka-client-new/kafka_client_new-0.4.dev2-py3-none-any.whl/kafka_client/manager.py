from abc import ABC, abstractmethod
import atexit
import logging
from prometheus_client import Summary, start_http_server
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler

from .handler import Handler, EmptyHandler
from .consumer import Consumer
from .producer import Producer
from .kafka_client_exception import KafkaClientException

HANDLE_TIME = Summary('handle_time', 'Time spent to handle batch')

logger = logging.getLogger(__name__)


class KafkaManager(ABC):
    @abstractmethod
    def set_handler(self, handler: Handler):
        pass

    @abstractmethod
    def run(self):
        pass


class DefaultBatchKafkaManager(KafkaManager):

    def __init__(self,
                 consumer: Consumer,
                 producer: Producer,
                 is_run_prometheus_server: bool = True,
                 prometheus_server_port: int = 8000,
                 interval_seconds: int = 60):
        self.consumer = consumer
        self.producer = producer
        self.handler: Handler = EmptyHandler()
        self.is_run_prometheus_server = is_run_prometheus_server
        self.prometheus_server_port = prometheus_server_port
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(
            self._send_metrics,
            trigger=IntervalTrigger(seconds=interval_seconds),
        )

    def set_handler(self, handler: Handler):
        self.handler = handler

    def run_prometheus_server(self):
        start_http_server(self.prometheus_server_port)

    def run(self):
        atexit.register(self.consumer.reset_offset)
        if self.is_run_prometheus_server:
            self.run_prometheus_server()
            self.scheduler.start()
            atexit.register(self.scheduler.shutdown)
        for batch in self.consumer.messages():
            try:
                handled_batch = self.handler.handle(batch)
                if self.producer:
                    self.producer.send(handled_batch)
                self.consumer.commit()
            except Exception as error:
                self.consumer.reset_offset()
                logger.exception(error)
                raise KafkaClientException() from error

    def _send_metrics(self):
        logger.info("Sending metrics")
        self.consumer._send_topic_metrics()

    @HANDLE_TIME.time()
    def _handle(self, batch):
        return self.handler.handle(batch)


class RoutingBatchManager(DefaultBatchKafkaManager):
    @classmethod
    def get_target(cls, msg):
        for edge in msg.value['route']:
            if edge['from']['topic_name'] == msg.from_topic:
                return [x['topic_name'] for x in edge['to']] if isinstance(edge['to'], list) \
                    else [edge['to']['topic_name']]

    def determine_topics(self, batch):
        for msg in batch:
            msg.to_topics = self.get_target(msg)
        return batch

    def run(self):
        atexit.register(self.consumer.reset_offset)
        if self.is_run_prometheus_server:
            self.run_prometheus_server()
            self.scheduler.start()
            atexit.register(self.scheduler.shutdown)
        for batch in self.consumer.messages():
            try:
                handled_batch = self.handler.handle(batch)
                splitted_messages = self.determine_topics(handled_batch)
                if self.producer:
                    self.producer.send(splitted_messages)
                self.consumer.commit()
            except Exception as error:
                self.consumer.reset_offset()
                logger.exception(error)
                raise KafkaClientException() from error
