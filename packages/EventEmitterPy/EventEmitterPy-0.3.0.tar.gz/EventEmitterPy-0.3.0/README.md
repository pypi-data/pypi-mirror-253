# EvenEmitter
Python library for event driven programming built on top of asyncio.


## Overview

The `EventEmitter` class allows you to create and manage events and event handlers in an asynchronous environment. It provides a simple mechanism to emit events and notify registered handlers.

## benchmark logging events 
the benchmarklogging.py file contains a simple benchmarking script that compares the performance of the EventEmitter class to the built-in asyncio.Event class. The benchmarking script creates 1 million events and 1 million handlers for each event. It then emits all events and measures the time it takes to complete. The benchmarking script can be run with the following command:

```bash
Benchmarking 1000000
Current memory usage is 199.879491MB; Peak was 199.879563MB
Emitted 1000000 in 32.328567299999996 seconds
```
The benchmark for 1 million events and 1 million handlers shows memory usage of 199.879491MB and a time of 32.328567299999996 seconds. This means that the event emitter is using 199.879491MB of memory and it took 32.328567299999996 seconds to emit 1 million events with 1 million handlers. Inside the handler logging is done to simulate the real world scenario.

```bash
## benchmark with api call
The  benchmarkapicall.py file contains a simple benchmarking script that compares the performance of the EventEmitter class to the built-in asyncio.Event class. The benchmarking script creates 1000 events and 1000 handlers for each event. It then emits all events and measures the time it takes to complete. The benchmarking script can be run with the following command:

```bash
$ python benchmarkapicall.py
```
results: 
1. 1 event 1 handler
```bash
    Benchmarking 1
    Current memory usage is 0.00052MB; Peak was 0.000592MB
    Emitted 1 in 0.4999799 seconds
```
The benchmark for 1 event and 1 handler shows memory usage of 0.00052MB and a time of 0.4999799 seconds. This means that the event emitter is using 0.00052MB of memory and it took 0.4999799 seconds to emit 1 event with 1 handler. Inside the handler asynchrouns  api  call made to simulate the real world scenario.

2. 1000 events 1 handler
```bash
    Benchmarking 1000
    Current memory usage is 0.183028MB; Peak was 0.1831MB
    Emitted 1000 in 8.076447499999999 seconds
```
The benchmark for 1000 events and 1 handler shows memory usage of 0.183028MB and a time of 8.076447499999999 seconds. This means that the event emitter is using 0.183028MB of memory and it took 8.076447499999999 seconds to emit 1000 events with 1 handler. Inside the handler asynchrouns  api  call made to simulate the real world scenario.

This means 
### Installation

```bash
pip install EventEmitterPy
```

### Example

```python
import asyncio
from collections import defaultdict
from EventEmitterPy.emitter import EventEmitter

# Example Usage
async def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

emitter = EventEmitter()
emitter.on('my_event', my_handler)
await emitter.emit('my_event', 1, 2, key='value') # Prints: Event 'my_event' received with arguments: (1, 2) and kwargs: {'key': 'value'}
```

## API Documentation

### `emit(event, *args, **kwargs)`

Emit an event and call all registered handlers.

- `event`: The name of the event.
- `args`: Additional positional arguments for the event handlers.
- `kwargs`: Additional keyword arguments for the event handlers.

```python
import asyncio

async def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for the 'my_event' event
emitter.on('my_event', my_handler)

# Emitting the 'my_event' event
await emitter.emit('my_event', 1, 2, key='value')
```

### `on(event, handler)`

Register an event handler.

- `event`: The name of the event.
- `handler`: The function to be called when the event is emitted.

```python
def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for the 'my_event' event
emitter.on('my_event', my_handler)
```

### `off(event, handler)`

Unregister an event handler.

- `event`: The name of the event.
- `handler`: The function to be unregistered.

```python
def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for the 'my_event' event
emitter.on('my_event', my_handler)

# Unregistering the handler for the 'my_event' event
emitter.off('my_event', my_handler)
```

### `removeAllListeners(event)`

Remove all listeners for the given event.

- `event`: The name of the event.

```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering multiple handlers for the 'my_event' event
emitter.on('my_event', lambda event: print(f"Handler 1 for '{event}'"))
emitter.on('my_event', lambda event: print(f"Handler 2 for '{event}'"))

# Removing all listeners for the 'my_event' event
emitter.removeAllListeners('my_event')
```



### `event_names()`

Return a list of all registered event names.

```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering handlers for different events
emitter.on('event1', lambda event: None)
emitter.on('event2', lambda event: None)

# Getting a list of all registered event names
events = emitter.event_names()
print("Registered events:", events)
```


### `listener_count(event)`

Return the number of listeners for the given event.

- `event`: The name of the event.

```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering multiple handlers for the 'my_event' event
emitter.on('my_event', lambda event: None)
emitter.on('my_event', lambda event: None)

# Getting the number of listeners for the 'my_event' event
count = emitter.listener_count('my_event')
print("Number of listeners for 'my_event':", count)
```

### `once(event, handler)`

Register a handler that will be called at most once.

- `event`: The name of the event.
- `handler`: The function to be called once.

```python
def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for the 'my_event' event that will be called once
emitter.once('my_event', my_handler)

# Emitting the 'my_event' event
await emitter.emit('my_event', 1, 2, key='value')
```


### `listeners(event)`

Return a list of all listeners for the given event.

- `event`: The name of the event.


```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering multiple handlers for the 'my_event' event
emitter.on('my_event', lambda event: None)
emitter.on('my_event', lambda event: None)

# Getting a list of all listeners for the 'my_event' event
listeners = emitter.listeners('my_event')
print("Listeners for 'my_event':", listeners)
```


### `rawListeners(event)`

Return a copy of the handlers for the given event.

- `event`: The name of the event.

```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering multiple handlers for the 'my_event' event
emitter.on('my_event', lambda event: None)
emitter.on('my_event', lambda event: None)

# Getting a copy of all handlers for the 'my_event' event
handlers_copy = emitter.rawListeners('my_event')
print("Copy of handlers for 'my_event':", handlers_copy)
```

### `prependListener(event, handler)`

Register a handler to be called before all others.

- `event`: The name of the event.
- `handler`: The function to be called first.

```python
def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for the 'my_event' event
emitter.on('my_event', my_handler)

# Registering a handler to be called before the existing handler
emitter.prependListener('my_event', lambda event: print(f"First handler for '{event}'"))

# Emitting the 'my_event' event
await emitter.emit('my_event', 1, 2, key='value')
```

### `setMaxListeners(event, n)`

Set the maximum number of listeners for all events. Default is 10.

- `event`: The name of the event.
- `n`: The maximum number of listeners.


```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Setting the maximum number of listeners for the 'my_event' event
emitter.setMaxListeners('my_event', 5)
```
### `getMaxListeners(event)`

Return the maximum number of listeners for an event.

- `event`: The name of the event.

```python
# Creating an instance of EventEmitter
emitter = EventEmitter()

# Setting the maximum number of listeners for the 'my_event' event
emitter.setMaxListeners('my_event', 5)

# Getting the maximum number of listeners for the 'my_event' event
max_listeners = emitter.getMaxListeners('my_event')
print("Max listeners for 'my_event':", max_listeners)
```

### `onAny(handler)`

Register a handler for all events.

- `handler`: The function to be called for all events.

```python
def my_handler(event, *args, **kwargs):
    print(f"Event '{event}' received with arguments: {args} and kwargs: {kwargs}")

# Creating an instance of EventEmitter
emitter = EventEmitter()

# Registering a handler for all events
emitter.onAny(my_handler)
```
