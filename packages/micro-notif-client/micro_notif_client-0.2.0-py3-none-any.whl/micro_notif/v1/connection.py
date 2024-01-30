import aio_pika
from aio_pika.abc import AbstractConnection


class AIOPikaConnectionProvider:
    connection_string: str
    _connection: AbstractConnection | None = None

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string

    async def get_connection(self) -> AbstractConnection:
        if not self._connection or self._connection.is_closed:
            self._connection = await aio_pika.connect_robust(
                self.connection_string
            )

        return self._connection

    async def close_connection(self) -> None:
        if not self._connection:
            raise ValueError("Connection not initialize!")

        if not self._connection.is_closed:
            await self._connection.close()
