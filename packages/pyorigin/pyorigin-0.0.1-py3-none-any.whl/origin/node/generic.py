import asyncio
from ..listners import ListnerManager
from ..packets import Packet

class Node(ListnerManager):
    def __init__(self, host, port):
        super().__init__()
        self.host, self.port = host, port
    
    async def _listen(self, connection):
        await self._run_event('connect', connection)

        while True:
            packet = await connection.recv()
            if not packet: break

            # run packet events
            await self._run_event('packet', connection, packet)
            await self._run_event(packet.headers.transaction, connection, packet)

            # run packet actions
            await self._run_packet(packet, connection, packet)
                

        await self._run_event('disconnect', connection)

    async def _start(self):
        raise NotImplementedError

    def start(self):
        asyncio.run(self._start())