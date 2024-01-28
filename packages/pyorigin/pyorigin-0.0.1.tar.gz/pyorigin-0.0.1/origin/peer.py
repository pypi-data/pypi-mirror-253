from .packets import Packet
import asyncio

class Peer:
    def __init__(self, reader, writer):
        self.reader, self.writer = reader, writer

    async def send(self, packet):
        # packet.headers.sender = self.node.id

        packet_bytes = packet.serialise()
        
        self.writer.write(Packet.preflight(packet_bytes))
        self.writer.write(packet_bytes)
        await self.writer.drain()

    async def recv(self):
        data = b''
        message_length = int.from_bytes(await self.reader.read(Packet.PREFLIGHT_SIZE), 'big')
        while True:
            chunk = await self.reader.read(Packet.CHUNK_SIZE)
            if not chunk: return None
            data += chunk
            if len(data) >= message_length: break

        data = Packet.deserialise(data)
        return data
    
    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()