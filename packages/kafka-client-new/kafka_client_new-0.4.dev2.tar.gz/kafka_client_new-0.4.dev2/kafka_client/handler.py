from abc import ABC, abstractmethod
from typing import Iterable

from .message import JSONMessage


class Handler(ABC):
    @abstractmethod
    def handle(self, data: Iterable[JSONMessage]):
        pass


class EmptyHandler(Handler):
    def handle(self, data: Iterable[JSONMessage]):
        return data
