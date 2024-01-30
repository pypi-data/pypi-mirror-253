import json
from dataclasses import dataclass, asdict


@dataclass
class CommunicationWrapper:
    common_id: str
    content: str

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, json_str: str) -> "CommunicationWrapper":
        data = json.loads(json_str)
        return cls(**data)
