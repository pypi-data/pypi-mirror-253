import base64


class StringDecoder:
    class _StringDecoder:
        def __init__(self, value: str) -> None:
            self._value: str = value

        def decode(self) -> str:
            try:
                decoded_bytes = base64.b64decode(self._value)
                decoded_str = decoded_bytes.decode("utf-8")
                return decoded_str
            except Exception:
                return self._value

    def __init__(self, value: str) -> None:
        self._value: str = value

    def decode(self) -> str:
        return self._StringDecoder(self._value).decode()
