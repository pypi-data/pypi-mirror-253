class RetryQueue:
    def __init__(self, header_value_match: int, ttl: int, dlx_exchange: str = ""):
        self.header_value_match: int = header_value_match
        self.ttl: int = ttl
        self.dlx_exchange: str = dlx_exchange

    @property
    def return_name(self) -> str:
        return f"retry.queue.{self.header_value_match}"
