import jwt
import json
from tamqp.models.communication_wrapper import CommunicationWrapper


class EncodedProvider:
    def __init__(self, key: str) -> None:
        self.key: str = key
        self.algorithm = "HS256"

    def encode(self, message: str, common_id: str) -> str:
        payload = {"CommonId": common_id, "Content": message}
        return jwt.encode(payload, self.key, algorithm=self.algorithm)

    def decode(self, message: str) -> CommunicationWrapper:
        try:
            payload = jwt.decode(message, self.key, algorithms=[self.algorithm])
            common_id = payload["CommonId"]
            content = payload["Content"]
            return CommunicationWrapper(common_id, content)
        except jwt.ExpiredSignatureError:
            raise Exception("Invalid message: Signature has expired.")
        except jwt.InvalidTokenError:
            raise Exception("Invalid message: Token verification failed.")
        except KeyError:
            raise Exception("Invalid message: Missing required payload fields.")
