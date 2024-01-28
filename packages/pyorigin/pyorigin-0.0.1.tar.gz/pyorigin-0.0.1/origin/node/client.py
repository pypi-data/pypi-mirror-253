import asyncio
from .generic import Node
from ..peer import Peer

class Client(Node):
    def __init__(self, host, port):
        super().__init__(host, port)

    async def _start(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        server = Peer(reader, writer)
        await self._listen(server)