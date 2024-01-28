class ListnerManager:
    def __init__(self):
        self._packets = []
        self._events = {}

    # Actions
    def packet(self, **headers):
        def decorator(func):
            self._packets.append({
                'rule': headers,
                'function': func
            })
            return func
        return decorator
    
    async def _run_packet(self, packet, *args):
        for action in self._packets:
            if all([packet.headers[key] == value for key, value in action['rule'].items()]):
                await action['function'](*args)

    # Events

    def on(self, event):
        def decorator(func):
            self._events[event] = func
            return func
        return decorator

    async def _run_event(self, event, *args):
        if event in self._events:
            await self._events[event](*args)