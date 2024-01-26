from enum import Enum
from typing import Optional, Callable


class Published(Enum):
    OK_PUBLISHED = 1
    ERROR_PUBLISHED = 2


class SubscriptionStatus(Enum):
    OK_SUBSCRIPTION = 1
    ERROR_SUBSCRIPTION = 2


class ExchangeType(Enum):
    TOPIC = "topic"
    HEADERS = "headers"
    FANOUT = "fanout"
    DIRECT = "direct"

    def exchange_type_to_string(self) -> str:
        return self.value


class Exchange:
    def __init__(
            self,
            name: str,
            exchange_type: ExchangeType = ExchangeType.TOPIC,
            durable: bool = True,
            auto_delete: bool = False,
            internal: bool = False
    ) -> None:
        self.name: str = name
        self.exchange_type: ExchangeType = exchange_type
        self.durable: bool = durable
        self.auto_delete: bool = auto_delete
        self.internal: bool = internal


class BindOptions:
    def __init__(self, exchange: Exchange, routing_key: Optional[str] = None) -> None:
        self.exchange: Exchange = exchange
        self.routing_key: Optional[str] = routing_key


class QueueSubscribed:
    def __init__(
            self,
            name: str,
            bind: Optional[BindOptions] = None,
            auto_ack_when_callback: bool = False,
            callback: Optional[Callable] = None
    ) -> None:
        self.name: str = name
        self.bind: Optional[BindOptions] = bind
        self.auto_ack_when_callback: bool = auto_ack_when_callback
        self.callback: Optional[Callable] = callback
