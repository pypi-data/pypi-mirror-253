import time
import pika
import uuid
from typing import Dict, Optional

from tamqp.models.amqp_init import AMQPInit
from tamqp.models.rabbit_library import Exchange, QueueSubscribed, ExchangeType
from tamqp.models.retry_queue import RetryQueue
from tamqp.services.amqp_provider_config import AMQPProviderConfig
from tamqp.services.amqp_utils import AMQPUtils
from tamqp.services.encoded_provider import EncodedProvider
from tamqp.utils.string_decoder import StringDecoder
from pika.spec import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel


class AMQPProvider(EncodedProvider, AMQPProviderConfig, AMQPUtils):
    def __init__(self, parameters: AMQPInit, key: str, max_connection_retries: int=3) -> None:
        super().__init__(key)
        self.content_type_text = "text/plain"
        self.parameters: AMQPInit = parameters
        self.destination_declared: bool = False
        self.key: str = parameters.encryption_key
        self.max_connection_retries = max_connection_retries

        self.connections: Dict[str, Optional[pika.BlockingConnection]] = {"consumer": None, "publisher": None}
        self.channels: Dict[str, Optional[BlockingChannel]] = {"consumer": None, "publisher": None}

        self.consumer_channel = self.channels["consumer"]
        self.publisher_channel = self.channels["publisher"]

        self.establish_connection_and_channels()

    def establish_connection_and_channels(self):
        retry_count = 0
        while True:
            try:
                self.connections["consumer"] = self.init_connection(self.parameters)
                self.connections["publisher"] = self.init_connection(self.parameters)
                self.channels["consumer"] = self.connections["consumer"].channel()
                self.channels["publisher"] = self.connections["publisher"].channel()
                self.consumer_channel = self.channels["consumer"]
                self.publisher_channel = self.channels["publisher"]
                break
            except Exception as e:
                if retry_count >= self.max_connection_retries:
                    print(f"Max retries {self.max_connection_retries} reached while attempting to establish connection.: {e}")
                    raise e
                retry_count += 1
                print(f"[{retry_count}/{self.max_connection_retries}] Error while establishing connection retrying...: {e}, ")
                time.sleep(5)  # Wait for 5 seconds before retrying

    def setup_retry_queue(self, queue: RetryQueue) -> None:
        queue_props = self.generate_props({AMQPProviderConfig.X_MESSAGE_TTL: queue.ttl, AMQPProviderConfig.X_DEAD_LETTER_EXCHANGE: queue.dlx_exchange})
        self.consumer_channel.queue_declare(queue.return_name, True, False, False, False, queue_props)

    def setup_retry_infrastructure(self) -> None:
        self.consumer_channel.exchange_declare(AMQPProviderConfig.RETRY_EXCHANGE, ExchangeType.DIRECT.value, True, False,
                                               arguments=self.generate_props({}))
        for queue in self.RETRY_QUEUES:
            self.setup_retry_queue(queue)
            header_props = self.generate_props({AMQPProviderConfig.X_MATCH: "all", str(queue.header_value_match): True})
            self.consumer_channel.queue_bind(queue.return_name, AMQPProviderConfig.RETRY_EXCHANGE, AMQPProviderConfig.DEFAULT_ROUTING_KEY, header_props)

    def setup_queue(self, queue: QueueSubscribed) -> None:
        self.declare_queue(queue.name)
        if queue.bind:
            bind_options = queue.bind
            self.declare_exchange(bind_options.exchange)
            self.bind_queue(queue.name, bind_options.exchange.name, bind_options.routing_key or "")
            print(
                f"BindQueue - channelId={self.consumer_channel.channel_number} queue={queue.name} exchange={bind_options.exchange.name} routingKey={bind_options.routing_key}")
        else:
            print(f"No binding options - channelId={self.consumer_channel.channel_number} queue={queue.name}")
        self.consume_queue(queue)

    def declare_queue(self, queue_name: str) -> None:
        self.consumer_channel.queue_declare(queue_name, True, False, False, None)

    def declare_exchange(self, exchange: Exchange) -> None:
        self.consumer_channel.exchange_declare(exchange.name, exchange.exchange_type.value, durable=exchange.durable,
                                               auto_delete=exchange.auto_delete, arguments=self.generate_props({}))

    def init_connection(self, parameters: AMQPInit) -> pika.BlockingConnection:
        # connection_credentials = pika.PlainCredentials(
        #     username=parameters.username,
        #     password=parameters.password,
        #     erase_on_connect=True
        # )
        #
        # connection_parameters = pika.ConnectionParameters(
        #     host=parameters.hostname,
        #     port=parameters.port,
        #     virtual_host=parameters.virtual_host,
        #     credentials=connection_credentials
        # )
        connection = self.generate_connection_factory(parameters)
        print(f"New AMQP connection created. connectionId={connection}")
        return connection

    # def is_sensitive_content(self, delivery: pika.spec.Basic.Deliver) -> bool:
    #     return bool(delivery.properties.headers.get(AMQPProviderConfig.SENSITIVE_CONTENT_KEY, False))

    def consume_queue(self, queue: QueueSubscribed) -> None:
        print(
            f"Subscribing to queue={queue.name} with autoAckWhenCallback={queue.auto_ack_when_callback} channelId={self.consumer_channel.channel_number}")

        def cb(channel, method, properties, body):
            try:
                message = self.decode(body.decode("UTF-8"))

                content = message.content

                print(
                    f"Received Message - channelId={self.consumer_channel.channel_number} tag={method.delivery_tag} RoutingKey={method.routing_key} Exchange={method.exchange} commonId={message.common_id} content={content}")

                if queue.callback:
                    queue.callback(message, method)

                if queue.auto_ack_when_callback:
                    self.ack_message(method)
            except Exception as ex:
                print(
                    f"Error processing message. channelId={self.consumer_channel.channel_number} tag={method.delivery_tag} message={ex}")

        def cancel(consumer_tag):
            pass

        # Code below is useful to debug
        #
        # method_frame, header_frame, body = self.consumer_channel.basic_get(queue.name)
        # if method_frame:
        #     print("Received message from", queue.name)
        #     print("Message body:", body)
        #     self.consumer_channel.basic_ack(method_frame.delivery_tag)
        # else:
        #     print("No message returned from", queue.name)

        self.consumer_channel.basic_consume(queue.name, cb, False)
        print(f"Successfully enrolled in queue={queue.name} channelId={self.consumer_channel.channel_number}")

        try:
            self.consumer_channel.start_consuming()
        except KeyboardInterrupt:
            self.consumer_channel.stop_consuming()

    def bind_queue(self, queue_name: str, exchange_name: str, routing_key: str) -> None:
        self.consumer_channel.queue_bind(queue_name, exchange_name, routing_key)

    def publish(self, routing_key: str, message: str, common_id: str = str(uuid.uuid4()),
                encoded: bool = True, exchange: Optional[Exchange] = None, sensitive_content: bool = False,
                delay: int = 0, logging_enabled: bool = False) -> None:
        try:
            try:
                if not self.connections["publisher"] or self.connections["publisher"].is_closed:
                    raise Exception("RabbitMQ connection is closed")
                self.connections["publisher"].process_data_events()
            except Exception as e:
                # Attempt to reconnect if connection is lost
                self.connections["publisher"] = self.init_connection(self.parameters)
                self.channels["publisher"] = self.connections["publisher"].channel()
                self.publisher_channel = self.channels["publisher"]

            self.declare_destination(routing_key, exchange)

            # headers = self.generate_props({SensitiveContentKey: sensitive_content})

            headers = self.generate_props({"x-delay": delay})

            message_properties = BasicProperties(content_type=self.content_type_text, headers=headers, delivery_mode=2)

            self.publisher_channel.basic_publish(
                exchange=exchange.name if exchange else AMQPProviderConfig.DEFAULT_EXCHANGE,
                routing_key=routing_key,
                body=self.encode(message, common_id) if encoded else message.encode(),
                properties=message_properties
            )

            content = StringDecoder(message).decode if sensitive_content else message

            if exchange and logging_enabled:
                print(
                    f"[Publish] message - channelId={self.publisher_channel.channel_number} exchange={exchange.name} type={exchange.exchange_type} routingKey={routing_key} commonId={common_id} content={content}")
            elif logging_enabled:
                print(
                    f"[Publish] message - channelId={self.publisher_channel.channel_number} queue={routing_key} commonId={common_id} content={content}")

        except Exception as e:
            if logging_enabled:
                print(
                    f"Failed to publish message to queue. channelId={self.publisher_channel.channel_number} commonId={common_id} error={e}")
            raise e

    def declare_destination(self, queue_name: str, exchange: Optional[Exchange]) -> None:
        if self.destination_declared:
            return

        if exchange:
            self.declare_exchange(exchange)
        else:
            self.declare_queue(queue_name)

        self.destination_declared = True

    def ack_message(self, delivery: pika.spec.Basic.Deliver) -> None:
        tag = delivery.delivery_tag
        print(f"Ack message. channelId={self.consumer_channel.channel_number} tag={tag}")
        self.consumer_channel.basic_ack(delivery.delivery_tag, False)

    def send_back(self, delivery: pika.spec.Basic.Deliver, routing_key: Optional[str] = None) -> None:
        self.ack_message(delivery)

        attempts = delivery.get_properties().headers.get(AMQPProviderConfig.RETRY_COUNT_HEADER, 0)
        current_attempt = 1 if attempts >= len(self.RETRY_QUEUES) else attempts + 1

        print(
            f"[sendBack] channelId={self.consumer_channel.channel_number} MaxNoOfRetries={AMQPProviderConfig.MAX_NO_OF_RETRIES} attempts={attempts} currentAttempt={current_attempt} deliveryRoutingKey={delivery.envelope.routing_key} routingKey={routing_key} tag={delivery.envelope.delivery_tag}")

        if attempts >= AMQPProviderConfig.MAX_NO_OF_RETRIES:
            self.publish(
                f"{delivery.routing_key}.dead_letter",
                delivery.decode(delivery.get_body()),
                encoded=False
                # sensitive_content=self.is_sensitive_content(delivery)
            )
            print(
                f"Sent dead letter. channelId={self.publisher_channel.channel_number} queue={routing_key or delivery.routing_key} tag={delivery.delivery_tag}")
        else:
            headers = self.generate_props({
                str(current_attempt): True,
                AMQPProviderConfig.RETRY_COUNT_HEADER: (attempts + 1)
                # SensitiveContentKey: self.is_sensitive_content(delivery)
            })
            properties = BasicProperties(content_type="text/plain", headers=headers, delivery_mode=2)

            print(
                f"[sendBack] - Publishing to RetryExchange. channelId={self.publisher_channel.channel_number} attempts={attempts} currentAttempt={current_attempt} headers={headers} properties={properties}")

            self.publisher_channel.basic_publish(
                exchange=AMQPProviderConfig.RETRY_EXCHANGE,
                routing_key=routing_key or delivery.routing_key,
                body=bytes(delivery.get_body()),
                properties=properties
            )
