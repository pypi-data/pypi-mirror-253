import logging
from typing import Callable
from pika.spec import Basic

from .models.communication_model import convert_to
from .models.test_model import TestMessageModel
from ..models.communication_wrapper import CommunicationWrapper
from ..services.amqp import AMQP


class JobConsumer:

    def __init__(self):
        self.logger = logging.getLogger('job_consumer')

    def handle_scrape_flight(self, rmq: AMQP) -> Callable[[CommunicationWrapper, Basic.Deliver], None]:
        def callback(wrapper: CommunicationWrapper, tag: Basic.Deliver) -> None:
            model = convert_to(wrapper.content, TestMessageModel)

            if model is not None:
                message = model.message
                if message:
                    self.logger.info(f"Received message to scrape flight for message={message}")
                    try:
                        # TODO: Create orchestration layer here to kick off scraper
                        print(f"Triggered flight scrape job for message={message}")
                        self.logger.info(f"Triggered flight scrape job for message={message}")
                        rmq.ack_message(tag)
                    except (ValueError, Exception) as e:
                        self.logger.error(f"Error in triggering flight scrape job for message={message}", e)
                        rmq.ack_message(tag)
                    return
                else:
                    self.logger.error("Message field is empty in TestMessageModel instance.")
            else:
                self.logger.error(
                    "Could not convert the dequeued message into a model. This is most likely a malformed "
                    "message.")
            rmq.ack_message(tag)

        return callback
