# Event Bus Implementation
class EventBus:
    def __init__(self):
        self.listeners = {}

    def register(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def dispatch(self, event):
        event_type = type(event)
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(event)

