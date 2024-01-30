from typing import Optional, Any
from dataclasses import dataclass
from typing import Optional


@dataclass
class JSONMessage:
    key: str
    value: dict
    from_topic: str
    to_topics: Optional[list]
