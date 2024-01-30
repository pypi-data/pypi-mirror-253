import json
import base64
import logging
from typing import Optional, TypeVar, Type, Generic

T = TypeVar('T')


class TaekusCommunicationModelBase:
    pass


class TaekusCommunicationModel(Generic[T]):

    def to_encoded_message(self) -> str:
        return to_message(self)

    @classmethod
    def to_model(cls: Type[T], input: str) -> Optional[T]:
        return convert_to(input, cls)


def encode(value: str) -> str:
    return base64.b64encode(value.strip().encode()).decode()


def convert_to(input: str, model_class: Type[T]) -> Optional[T]:
    logger = logging.getLogger('communication_writer')
    try:
        decoded = base64.b64decode(input).decode()
        return model_class(**json.loads(decoded))
    except Exception as ex:
        try:
            decoded = base64.b64decode(input).decode()
            logger.error(f"Message could not be converted to model as there was a mismatch: {decoded}", exc_info=True)
        except Exception as ex:
            logger.error(f"Message sent was not base64 decoded. value={input}", exc_info=True)
    return None


def to_message(value: T) -> str:
    if not isinstance(value, TaekusCommunicationModelBase):
        raise TypeError('value must be a TaekusCommunicationModelBase')
    return encode(json.dumps(value.__dict__))
