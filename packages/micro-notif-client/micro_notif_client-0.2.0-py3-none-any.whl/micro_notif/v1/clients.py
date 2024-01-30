import json

import aio_pika
from aio_pika.abc import AbstractConnection
from aio_pika import ExchangeType


from .utils import get_exchange
from .types import SMSEventDict
from .connection import AIOPikaConnectionProvider

NOTIFY_EXCHANGE_TYPE = ExchangeType.DIRECT


class MicroNotifRabbitMQClient:
    _base_routing_key: str = "micro_notif.v1"

    _exchange_name: str
    _durable: bool

    _connection_provider: AIOPikaConnectionProvider
    _connection: AbstractConnection

    connected: bool = False

    def __init__(self, conn_str: str, exchange_name: str, durable: bool):
        self._connection_provider = AIOPikaConnectionProvider(
            connection_string=conn_str
        )
        self._exchange_name = exchange_name
        self._durable = durable

    async def connect(self):
        self._connection = await self._connection_provider.get_connection()
        self.connected = True

    async def disconnect(self):
        await self._connection_provider.close_connection()
        self.connected = False

    async def send_sms(self, message: SMSEventDict):
        async with get_exchange(
            connection=self._connection,
            exchange_name=self._exchange_name,
            exchange_type=ExchangeType.DIRECT,
            durable=self._durable,
        ) as exchange:
            await exchange.publish(
                message=aio_pika.Message(body=json.dumps(message).encode()),
                routing_key=f"{self._base_routing_key}.notify.sms",
            )
