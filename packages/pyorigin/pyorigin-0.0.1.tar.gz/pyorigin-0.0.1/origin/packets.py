import uuid, json

class dotdict(dict):
    def __getattr__(self, item):
        value = self.get(item)
        if isinstance(value, dict):
            return dotdict(value)
        return value

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        del self[item]
    
    def copy(self):
        return dotdict(super().copy())

class Packet:
    CHUNK_SIZE = 1024
    PREFLIGHT_SIZE = 4

    def __init__(self, headers, body):
        self.headers = dotdict(headers)
        self.body = dotdict(body)

    @staticmethod
    def preflight(bytes): # get length of packet
        return len(bytes).to_bytes(Packet.PREFLIGHT_SIZE, 'big')
    
    def serialise(self): # serialise packet to bytes
        packet = json.dumps({
            'headers': self.headers,
            'body': self.body
        }).encode()
        return packet
    
    @staticmethod
    def deserialise(bytes): # deserialise bytes to packet
        data = bytes.decode()
        data = json.loads(data)
        return Packet(data['headers'], data['body'])

    def copy(self):
        return Packet(self.headers.copy(), self.body.copy())

    def response(self, body):
        response = self.copy()
        response.headers.transaction = 'response'
        response.headers.sender, response.headers.target = response.headers.target, response.headers.sender
        response.body = body
        return response