

class KafkaClientException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__()
