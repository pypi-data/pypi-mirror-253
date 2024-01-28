import asyncio
from .generic import Node
from ..peer import Peer

class Server(Node):
    def __init__(self, host, port):
        super().__init__(host, port)

    async def _listen(self, reader, writer):
        client = Peer(reader, writer)
        await super()._listen(client)

    async def _start(self):
        server = await asyncio.start_server(self._listen, self.host, self.port)
        await self._run_event('start')
        await server.serve_forever()