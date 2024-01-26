import asyncio

from collections import defaultdict
class EventEmitter:
    def __init__(self):
        self._event_handlers = defaultdict(list)
        self.event_max_listeners = defaultdict(int)

    async def emit(self, event, *args, **kwargs):
        """Emit an event and call all handlers."""
        # named events
        handlers = self._event_handlers.get(event, [])
        coroutines = [handler(*args, **kwargs) for handler in handlers]
        # any events
        any_handlers = self._event_handlers.get('*', [])
        any_coroutines = [handler(event, *args, **kwargs) for handler in any_handlers]
        coroutines.extend(any_coroutines)
        await asyncio.gather(*coroutines)

    def on(self, event, handler):
        """Register an event handler. If max listerners is reached, raise an exception."""
        if event not in self.event_max_listeners:
            self.event_max_listeners[event] = 10
        if len(self._event_handlers[event]) >= self.event_max_listeners[event]:
            raise Exception("Max listeners reached")
        else :
            if event not in self._event_handlers:
                self._event_handlers[event] = []
            self._event_handlers[event].append(handler)

    def off(self, event, handler):
        """Unregister an event handler."""
        if event in self._event_handlers:
            self._event_handlers[event].remove(handler)
    
    def removeAllListeners(self, event):
        """Remove all listeners for the given event."""
        self._event_handlers[event] = []

    def event_names(self):
        """Return a list of all registered event names."""
        return list(self._event_handlers.keys())
    
    def listener_count(self, event):
        """Return the number of listeners for the given event."""
        return len(self._event_handlers.get(event, []))
    
    def once(self, event, handler):
        """Register a handler that will be called at most once."""
        def wrapper(*args, **kwargs):
            self.off(event, wrapper)
            return handler(*args, **kwargs)
        self.on(event, wrapper)
    
    def listeners(self, event):
        """Return a list of all listeners for the given event."""
        return self._event_handlers.get(event, [])
    
    def rawListeners(self, event):
        """Return a copy of the handlers for the given event."""
        return self.listeners(event).copy()
    
    def prependListener(self, event, handler):
        """Register a handler to be called before all others."""
        if event not in self._event_handlers:
            self._event_handlers[event] = []
        self._event_handlers[event].insert(0, handler)

    def setMaxListeners(self, event, n):
        """Set the maximum number of listeners for all events."""
        self.event_max_listeners[event] = n

    def getMaxListeners(self, event):
        """Return the maximum number of listeners for all events."""
        return self.event_max_listeners[event]

    def onAny(self, handler):
        """Register a handler for all events."""
        self.on('*', handler)

        
