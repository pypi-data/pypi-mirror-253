from typing import AsyncGenerator
from contextlib import asynccontextmanager

from aio_pika import ExchangeType
from aio_pika.abc import AbstractConnection, AbstractExchange


@asynccontextmanager
async def get_exchange(
    connection: AbstractConnection,
    exchange_name: str,
    exchange_type: ExchangeType,
    durable: bool,
) -> AsyncGenerator[AbstractExchange, None]:
    channel = await connection.channel()

    try:
        exchange = await channel.declare_exchange(
            name=exchange_name, type=exchange_type, durable=durable
        )

        yield exchange
    finally:
        await channel.close()
