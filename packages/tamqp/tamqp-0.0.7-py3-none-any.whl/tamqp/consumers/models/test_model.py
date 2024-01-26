import uuid
from dataclasses import dataclass

from .communication_model import TaekusCommunicationModelBase, TaekusCommunicationModel


@dataclass
class TestMessageModel(TaekusCommunicationModelBase):
    job_id: str
    message: str


class TestMessage(TaekusCommunicationModel):
    queue_name: str = "TEST-QUEUE"
