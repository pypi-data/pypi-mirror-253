import logging
from typing import List
from tamqp.models.amqp_init import AMQPInit
from tamqp.services.amqp_provider import AMQPProvider


class AMQP(AMQPProvider):
    def __init__(self, parameters: AMQPInit, subscriptions=None) -> None:
        super().__init__(parameters, key="taekus_key")
        if subscriptions is None:
            subscriptions = []
        self.parameters = parameters
        self.subscriptions = subscriptions

        self.setup_retry_infrastructure()

    def subscribe(self) -> List[None]:
        results = []
        for queue in self.subscriptions:
            while True:
                try:
                    self.setup_queue(queue)
                    logging.info(
                        f"Successfully initialized - channelId={self.consumer_channel.channel_number}  queue={queue.name}")
                    results.append(None)
                    break  # Break the loop if the operation was successful.
                except Exception as ex:
                    logging.error(
                        f"Failed to subscribe - channelId={self.consumer_channel.channel_number}  queue={queue.name} error={ex}")
                    self.establish_connection_and_channels()  # Reconnect and try again.
        return results


    def close(self) -> None:
        try:
            for _, channel in self.channels.items():
                if channel.is_open:
                    channel.close()

            for _, conn in self.connections.items():
                if conn.is_open:
                    conn.close(self.CLOSING_TIMEOUT)

            logging.info("[AMQP] Closed Connection - Successfully")
        except Exception as ex:
            logging.error(f"[AMQP] Error Closing Connection - error={ex}")

