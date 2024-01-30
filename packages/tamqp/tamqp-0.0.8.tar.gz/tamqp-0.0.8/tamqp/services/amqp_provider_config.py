from typing import List

from tamqp.models.retry_queue import RetryQueue


class AMQPProviderConfig:
    RETRY_COUNT_HEADER = "x-retries"
    X_MATCH = "x-match"
    X_MESSAGE_TTL = "x-message-ttl"
    X_DEAD_LETTER_EXCHANGE = "x-dead-letter-exchange"
    DEFAULT_EXCHANGE = ""
    DEFAULT_ROUTING_KEY = ""
    DEFAULT_TAEKUS_KEY = "taekus_key"
    RETRY_EXCHANGE = "retry.exchange"
    DEAD_LETTER_QUEUE = "retry.dead_letter"
    SENSITIVE_CONTENT_KEY = "SensitiveContent"
    SENSITIVE_REDACTED_MESSAGE = "Message was redacted due to sensitive information."

    MAX_NO_OF_RETRIES: int = 25
    CLOSING_TIMEOUT: int = int(30000)
    RETRY_QUEUES: List[RetryQueue] = [
        RetryQueue(1, 10000),
        RetryQueue(2, 60000),
        RetryQueue(3, 300000),
        RetryQueue(4, 900000),
        RetryQueue(5, 1800000)
    ]
