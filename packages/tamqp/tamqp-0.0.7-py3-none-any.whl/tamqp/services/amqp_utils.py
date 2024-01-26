import pika
import ssl
from typing import Any, Dict
from tamqp.models.amqp_init import AMQPInit


class AMQPUtils:
    def generate_props(self, input: Dict[str, Any]) -> Dict[str, Any]:
        properties = {}
        for key, value in input.items():
            properties[key] = value
        return properties

    def generate_connection_factory(self, parameters):
        credentials = pika.PlainCredentials(parameters.username, parameters.password)

        ssl_options = None
        if parameters.is_tls:
            ssl_options = pika.SSLOptions(ssl.create_default_context(ssl.Purpose.CLIENT_AUTH))

        params = pika.ConnectionParameters(
            heartbeat=300,
            host=parameters.hostname,
            port=parameters.port,
            virtual_host=parameters.virtual_host or '/',
            credentials=credentials,
            ssl_options=ssl_options
        )

        return pika.BlockingConnection(params)
