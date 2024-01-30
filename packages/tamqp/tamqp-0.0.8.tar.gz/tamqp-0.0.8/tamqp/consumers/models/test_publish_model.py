import uuid
from dataclasses import dataclass

from .communication_model import TaekusCommunicationModelBase, TaekusCommunicationModel


@dataclass
class TestPublishMessageModel(TaekusCommunicationModelBase):
    job_id: str
    message: str


class TestPublishMessage(TaekusCommunicationModel):
    queue_name: str = "TEST-PUBLISH-QUEUE"
