from abc import ABC, abstractmethod


class CommunicationObject(ABC):

    @property
    @abstractmethod
    def queue_name(self) -> str:
        pass
