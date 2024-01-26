from typing import Optional


class AMQPInit:
    def __init__(
            self,
            username: str,
            password: str,
            hostname: str,
            port: int = 5672,
            virtual_host: Optional[str] = "/",
            encryption_key: Optional[str] = "taekus_key",
            is_tls: bool = False
    ) -> None:
        if not username:
            raise ValueError("username is null or empty")
        if not password:
            raise ValueError("password is null or empty")
        if not hostname:
            raise ValueError("hostname is null or empty")

        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.virtual_host = virtual_host
        self.encryption_key = encryption_key
        self.is_tls = is_tls

    @classmethod
    def from_args(cls, username: str, password: str, hostname: str, port: int, virtual_host: str,
                  encryption_key: str) -> "AMQPInit":
        vh = virtual_host if virtual_host.startswith("/") else f"/{virtual_host}"
        return cls(username, password, hostname, port, virtual_host=vh, encryption_key=encryption_key)

    @classmethod
    def from_args_and_virtual_host(cls, username: str, password: str, hostname: str, port: int,
                                   virtual_host: str) -> "AMQPInit":
        vh = virtual_host if virtual_host.startswith("/") else f"/{virtual_host}"
        return cls(username, password, hostname, port, virtual_host=vh)
