import logging
from abc import ABC, abstractmethod

from prometheus_client import Counter, Gauge
from kafka import KafkaConsumer

from .message import JSONMessage

logger = logging.getLogger(__name__)


class Consumer(ABC):

    def __init__(self, topics, consumer_settings, timeout_ms=20000, max_records=100):
        self.consumer = KafkaConsumer(*topics, **consumer_settings)
        self.message_read_counter = Counter('consumer_read_messages_total', 'Number of read messages')
        self.consumer_offset_messages_number = Gauge(
            name=f'consumer_offset_messages_number',
            documentation='Current value of consumer offset in specific partition',
            labelnames=['topic', 'partition'],
        )
        self.kafka_offset = Gauge(
            name=f'kafka_offset_messages_number',
            documentation='Current value of offset partition',
            labelnames=['topic', 'partition'],
        )
        self.timeout_ms = timeout_ms
        self.max_records = max_records

    def reset_offset(self):
        """
        In case of error during handling it is necessary to keep offsets positions before polling
         - get all consumers assignments
         - load last committed offsets
         - seek to last committed offsets
        """
        logger.debug('Reset offset')
        assignments = self.consumer.assignment()
        for assignment in assignments:
            logger.debug(
                f'Position before seek: {self.consumer.position(assignment)} for assigment {assignment}')
            last_committed_offset = self.consumer.committed(assignment)
            self.consumer.seek(assignment, last_committed_offset or 0)
            logger.debug(f'Last committed offset: {last_committed_offset}')
            logger.debug(f'Position after seek: {self.consumer.position(assignment)}')

    def commit(self):
        logger.debug('Commit offset')
        self.consumer.commit()

    def messages(self):

        def build_json_message(msg, topic):
            return JSONMessage(key=msg.key, value=msg.value, from_topic=topic, to_topics=None)

        while True:
            logger.debug('Start polling')
            batch = self.consumer.poll(
                timeout_ms=self.timeout_ms,
                max_records=self.max_records,
                update_offsets=True,
            )

            logger.debug('Finish polling')
            for topic_partition, messages in batch.items():
                self.message_read_counter.inc(len(messages))
                logger.debug(f'Fetch {len(messages)} messages for topic {topic_partition}')
                yield [build_json_message(msg, topic_partition.topic) for msg in messages]

    def _send_topic_metrics(self):
        for _, committed_offset, last_offset, assignment in self._get_offsets():
            self.consumer_offset_messages_number.labels(assignment.topic, str(assignment.partition)).set(committed_offset)
            self.kafka_offset.labels(assignment.topic, str(assignment.partition)).set(last_offset)

    def _get_offsets(self):
        assignments = self.consumer.assignment()
        last_offsets = self.consumer.end_offsets(list(assignments))
        for assignment in assignments:
            position_offset = self.consumer.position(assignment)
            committed_offset = self.consumer.committed(assignment)
            committed_offset = committed_offset if committed_offset else 0
            last_offset = last_offsets[assignment]
            yield position_offset, committed_offset, last_offset, assignment


class DefaultBatchConsumer(Consumer):

    def __init__(self, topic, consumer_settings, timeout_ms=20000, max_records=100):
        super().__init__([topic], consumer_settings, timeout_ms, max_records)
        self.topic = topic
        logger.info(f'DefaultBatchConsumer:\n'
                    f'\ttopic: {self.topic}\n'
                    f'\ttimeout_ms: {self.timeout_ms}\n'
                    f'\tmax_records: {self.max_records}\n'
                    f'\tconsumer group id: {consumer_settings["group_id"]}\n')


class MultiTopicBatchConsumer(Consumer):

    def __init__(self, topics, consumer_settings, timeout_ms=20000, max_records=100):
        super().__init__(topics, consumer_settings, timeout_ms, max_records)
        self.topics = topics
        logger.info(f'DefaultBatchConsumer:\n'
                    f'\ttopics: {self.topics}\n'
                    f'\ttimeout_ms: {self.timeout_ms}\n'
                    f'\tmax_records: {self.max_records}\n'
                    f'\tconsumer group id: {consumer_settings["group_id"]}\n')
